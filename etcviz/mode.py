"""
ETC Mode object.
"""
import os


default_knobs = {1: 0.5, 2: 0.5, 3: 0.5, 4: 0.5, 5: 0.5}


class Mode:
    def __init__(self, mode_dir, knobs=default_knobs):
        """
        Initialize a ETC Mode object.
        """
        self.dir = os.path.abspath(mode_dir)
        dir_name = os.path.split(self.dir)[1]
        self.name = dir_name.replace(" ", "").replace("-", "_")
        self.libname = f"{self.name}.main"
        self.knobs = knobs
