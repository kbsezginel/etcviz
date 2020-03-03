"""
ETC Mode object.
"""
import os


default_knobs = [0.5, 0.5, 0.5, 0.5, 0.5]


class Mode:
    def __init__(self, mode_dir, knobs=default_knobs):
        """
        Initialize a ETC Mode object.
        """
        self.dir = os.path.abspath(mode_dir)
        dir_name = os.path.split(self.dir)[1]
        self.name = dir_name.replace(" ", "").replace("-", "_")
        self.libname = f"{self.name}.main"
        self.knob1 = knobs[0]
        self.knob2 = knobs[1]
        self.knob3 = knobs[2]
        self.knob4 = knobs[3]
        self.knob5 = knobs[4]
