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
    Mode Development Tools
    =======================================
        """,
        epilog="""
    Example:
    > etcviz ETC_Mode
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    # Positional arguments
    parser.add_argument('mode', type=str,
                        help="Filename or directory of the ETC mode")

    # Optional arguments
    parser.add_argument('-r', '--record', type=int,
                        help="Record out to image sequence for ffmpeg")
    parser.add_argument('-k', '--knobs', default=[0.5, 0.5, 0.5, 0.2, 0.5],
                        type=float, metavar='', nargs=5,
                        help="ETC knob settings (ex: 0.5 0.5 0.5 0.2 0.5)")
    parser.add_argument('-g', '--gif', type=str,
                        help="Save image sequence as gif file")
    args = parser.parse_args()

    # Import the ETC mode script
    etc_mode = importlib.import_module(args.mode.split('.py')[0])
    knobs = {i: k for i, k in enumerate(args.knobs, start=1)}
    img_dir = 'imageseq'

    running = True
    recording = False

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

    etc = ETC()

    # initialize to ETC's resolution
    screenWidth, screenHeight = 1280, 720
    pygame.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    etc_mode.setup(screen, etc)

    while running:
        screen.fill((0, 0, 0, 255))
        etc_mode.draw(screen, etc)

        key = pygame.key.get_pressed()
        etc.update_knobs(key, knobs)
        if key[pygame.K_q]:
            exit()
        if key[pygame.K_SPACE]:
            etc.audio_trig = True
        if key[pygame.K_z]:
            etc.audio_trig = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if you try to quit, let's leave this loop
                running = False
        pygame.display.flip()

        if recording and counter < n_frames:
            pygame.image.save(screen, "imageseq/%05d.jpg" % counter)
            counter += 1
        elif recording and counter == n_frames:
            if args.gif:
                images_to_gif(img_dir, args.gif)
            exit()
