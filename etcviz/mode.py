"""
ETC Mode object.
"""

default_knobs = [0.5, 0.5, 0.5, 0.5, 0.5]


class Mode:
    def __init__(self, name="etcviz", knobs=default_knobs):
        """
        Initialize a ETC Mode object.
        """
        self.name = name
        self.knob1 = knobs[0]
        self.knob2 = knobs[1]
        self.knob3 = knobs[2]
        self.knob4 = knobs[3]
        self.knob5 = knobs[4]
