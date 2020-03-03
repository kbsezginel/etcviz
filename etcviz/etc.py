"""
ETC object.
"""
import os
import math
import pygame
import random
import shutil
import importlib
from .mode import Mode
from .tools import read_csv


class ETC:
    def __init__(self, modes, scenes=None):
        """
        Initialize a ETC object.
        """
        self.knob1 = 0.5
        self.knob2 = 0.5
        self.knob3 = 0.5
        self.knob4 = 0.5
        self.knob5 = 0.5
        self.knob_step = 0.01
        self.audio_in = [random.randint(-32768, 32767) for i in range(100)]
        self.bg_color = (0, 0, 0)
        self.audio_trig = False
        self.midi_note_new = False
        self.resolution = (1280, 720)
        self.screen = pygame.display.set_mode(self.resolution)
        self.wd = "etctmp"
        self.read_modes(modes)
        self.init_workdir()
        self.mode_index = 0
        self.setup_mode()
        if scenes is not None:
            self.read_scenes(scenes)


    def init_workdir(self):
        """
        Initialize a temporary work directory for ETC to use importlib.
        """
        # Create workdir if not exists (delete if exists)
        if os.path.exists(self.wd):
            shutil.rmtree(self.wd)
        os.mkdir(self.wd)
        # Copy all mode files
        for mode in self.modes:
            mode.root = os.path.join(self.wd, mode.name)
            mode.libname = f"{self.wd}.{mode.name}.main"
            shutil.copytree(mode.dir, mode.root)

    def read_modes(self, mode):
        """
        Read mode(s) from a given directory.
        Initially checks if there is a 'main.py' file in the given directory.
        If there is only loads that mode, if not checks each directory
        in given directory and collects the ones with 'main.py' files.
        """
        self.modes = []
        modes_list = os.listdir(mode)
        if "main.py" in modes_list:
            self.modes = [Mode(mode)]
        if self.modes == []:
            for m in modes_list:
                mdir = os.path.join(mode, m)
                if os.path.isdir(mdir):
                    if "main.py" in os.listdir(mdir):
                        self.modes.append(Mode(mdir))

    def setup_mode(self):
        """
        Load mode and setup display.
        """
        self.mode = importlib.import_module(self.modes[self.mode_index].libname)
        self.mode_root = self.modes[self.mode_index].root
        self.mode.setup(self.screen, self)
        print(f"Load mode {self.mode_index} / {len(self.modes)} : {self.modes[self.mode_index].name}")

    def load_next_mode(self):
        """
        Load next mode in the list.
        """
        self.mode_index += 1
        if self.mode_index >= len(self.modes):
            self.mode_index = 0
        self.setup_mode()

    def load_previous_mode(self):
        """
        Load previous mode in the list.
        """
        self.mode_index -= 1
        if self.mode_index <= 0:
            self.mode_index = len(self.modes) - 1
        self.setup_mode()

    def color_picker(self):
        """
        Original color_picker function from ETC. See link below:
        https://github.com/critterandguitari/ETC_Mother/blob/master/etc_system.py
        """
        # convert knob to 0-1
        c = float(self.knob4)

        # all the way down random bw
        rando = random.randrange(0, 2)
        color = (rando * 255, rando * 255, rando * 255)

        # random greys
        if c > .02 :
            rando = random.randrange(0,255)
            color = (rando, rando, rando)
        # grey 1
        if c > .04 :
            color = (50, 50, 50)
        # grey 2
        if c > .06 :
            color = (100, 100 ,100)
        # grey 3
        if c > .08 :
            color = (150, 150 ,150)
        # grey 4
        if c > .10 :
            color = (150, 150 ,150)

        # grey 5
        if c > .12 :
            color = (200, 200 ,200)
        # white
        if c > .14 :
            color = (250, 250 ,250)
        #colors
        if c > .16 :
            r = math.sin(c * 2 * math.pi) * .5 + .5
            g = math.sin(c * 4 * math.pi) * .5 + .5
            b = math.sin(c * 8 * math.pi) * .5 + .5
            color = (r * 255,g * 255,b * 255)
        # full ranoms
        if c > .96 :
            color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        # primary randoms
        if c > .98 :
            r = random.randrange(0, 2) * 255
            g = random.randrange(0, 2) * 255
            b = random.randrange(0, 2) * 255
            color = (r,g,b)

        color2 = (color[0], color[1], color[2])
        return color2

    def color_picker_bg(self):
        """
        Original color_picker_bg function from ETC. See link below:
        https://github.com/critterandguitari/ETC_Mother/blob/master/etc_system.py
        """
        c = self.knob5
        r = (1 - (math.cos(c * 3 * math.pi) * .5 + .5)) * c
        g = (1 - (math.cos(c * 7 * math.pi) * .5 + .5)) * c
        b = (1 - (math.cos(c * 11 * math.pi) * .5 + .5)) * c

        color = (r * 255,g * 255,b * 255)

        self.bg_color = color
        return color

    def update_knobs(self, key, knobs):
        """
        Update knobs but pressing a number between 1 - 4 and up/down keys together
        """
        for knob_id in range(1, 6):
            if key[getattr(pygame, f"K_{knob_id}")] and key[pygame.K_UP]:
                knobs[knob_id] += self.knob_step
                knobs[knob_id] = min(knobs[knob_id], 1.0)
                setattr(self, f"knob{knob_id}", knobs[knob_id])
            if key[getattr(pygame, f"K_{knob_id}")] and key[pygame.K_DOWN]:
                knobs[knob_id] -= self.knob_step
                knobs[knob_id] = max(knobs[knob_id], 0.0)
                setattr(self, f"knob{knob_id}", knobs[knob_id])

    def read_scenes(self, scenes_csv):
        """
        Read ETC Scenes.csv file modes
        """
        scenes = read_csv(scenes_csv)
        print(f'Reading scenes file: {scenes_csv}')
        self.scenes = []
        for idx, scene in enumerate(scenes):
            mode = Mode(name=scene[0], knobs=scene[1:6])
            self.scenes.append(mode)
