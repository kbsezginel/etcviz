"""
ETC command line interface.
"""
import os
import pygame
import argparse
import importlib
from .etc import ETC
from .tools import images_to_gif


def main():
    parser = argparse.ArgumentParser(
        description="""
    ============================== o   o ==
    ███████╗████████╗ ██████╗       \ /
    ██╔════╝╚══██╔══╝██╔════╝  ╔═════╩════╗
    █████╗     ██║   ██║       ║ ╦  ╦╦╔═╗ ║
    ██╔══╝     ██║   ██║       ║ ╚╗╔╝║╔═╝ ║
    ███████╗   ██║   ╚██████╗  ║  ╚╝ ╩╚═╝ ║
    ╚══════╝   ╚═╝    ╚═════╝  ╚══════════╝
    Critter & Guitari ETC Video Synthesizer
    Development and Visualization Tools
    =======================================
        """,
        epilog="""
    Example:
    > etcviz ETC_Mode
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    # Positional arguments
    parser.add_argument('mode', type=str,
                        help="Directory of the ETC mode(s)")

    # Optional arguments
    parser.add_argument('-r', '--record', type=int,
                        help="Record out to image sequence for ffmpeg")
    parser.add_argument('-k', '--knobs', default=[0.5, 0.5, 0.5, 0.2, 0.5],
                        type=float, metavar='', nargs=5,
                        help="ETC knob settings (ex: 0.5 0.5 0.5 0.2 0.5)")
    parser.add_argument('-g', '--gif', type=str,
                        help="Save image sequence as gif file")
    parser.add_argument('-rs', '--scenes', type=str,
                        help="Read ETC Scenes.csv file")
    parser.add_argument('--scale', type=float, default=1.0,
                        help="Scale screen resolution")
    args = parser.parse_args()

    pygame.init()
    pygame.key.set_repeat(0)
    # Initialize ETC
    resolution = (int(1280 * args.scale), int(720 * args.scale))
    etc = ETC(args.mode, scenes=args.scenes, resolution=resolution)

    knobs = {i: k for i, k in enumerate(args.knobs, start=1)}
    img_dir = 'imageseq'

    running = True
    recording = False
    counter = 0

    if args.record or args.gif:
        recording = True
    if args.record is None:
        n_frames = 30
    else:
        n_frames = args.record

    if recording:
        if not os.path.exists(img_dir):
            os.makedirs(img_dir)
        else:
            raise Exception(f"Image directory {img_dir} already exists, quitting!")
        counter = 0

    # MAIN LOOP ----------------------------------------------------------------
    while running:
        key = pygame.key.get_pressed()

        etc.screen.fill((0, 0, 0, 255))
        try:
            etc.mode.draw(etc.screen, etc)
        except Exception as e:
            print(e)
            print(f"Skipping mode {etc.mode_index}: {etc.modes[etc.mode_index].name}")
            etc.load_next_mode()

        etc.display_help()
        etc.display_levels()
        etc.audio_stream()

        # Update knobs
        for knob_id in range(1, 6):
            if key[getattr(pygame, f"K_{knob_id}")] and key[pygame.K_UP]:
                knobs[knob_id] += etc.knob_step
                knobs[knob_id] = min(knobs[knob_id], 1.0)
            if key[getattr(pygame, f"K_{knob_id}")] and key[pygame.K_DOWN]:
                knobs[knob_id] -= etc.knob_step
                knobs[knob_id] = max(knobs[knob_id], 0.0)
        etc.update_knobs(knobs)

        if key[pygame.K_0] and key[pygame.K_UP]:
            etc.audio_level += 0.01
            etc.audio_level = min(etc.audio_level, 1.0)
        if key[pygame.K_0] and key[pygame.K_DOWN]:
            etc.audio_level -= 0.01
            etc.audio_level = max(etc.audio_level, 0.0)
        if key[pygame.K_q]:
            exit()
        if key[pygame.K_s]:
            pygame.image.save(etc.screen, f"{mode_name}-screenshot.jpg")
        if key[pygame.K_r]:
            pygame.image.save(etc.screen, os.path.join(img_dir, '%05d.jpg' % counter))
            counter += 1
        elif counter != 0:
            images_to_gif(img_dir, f"{mode_name}-screencast.gif")
            counter = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if you try to quit, let's leave this loop
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    etc.load_next_mode()
                if event.key == pygame.K_LEFT:
                    etc.load_previous_mode()
                if event.key == pygame.K_a:
                    etc.save_mode()
                if event.key == pygame.K_w:
                    etc.write_scenes('Scenes.csv')
                if event.key == pygame.K_h:
                    etc.toggle("help")
                if event.key == pygame.K_l:
                    etc.toggle("levels")
                if event.key == pygame.K_SPACE:
                    etc.toggle("audio_trig")
        pygame.display.flip()

        if recording and counter < n_frames:
            pygame.image.save(etc.screen, os.path.join(img_dir, '%05d.jpg' % counter))
            counter += 1
        elif recording and counter == n_frames:
            if args.gif:
                images_to_gif(img_dir, args.gif)
            exit()
