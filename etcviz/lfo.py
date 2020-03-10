"""
LFO object.
"""
import math


class LFO:
    def __init__(self, shape="sine", frequency=10):
        """Initialize an LFO object with wave shape and frequency in Hz"""
        self.shape = shape
        self.step_size = 0.001 # seconds
        self.frequency = frequency
        self.wavetable = []
        self.index = 0
        if shape == "square":
            self.square()
        if shape == "triangle":
            self.triangle()
        if shape == "sine":
            self.sine()

    def __len__(self):
        """Return length of LFO wavetable"""
        return len(self.wavetable)

    def __iter__(self):
        """LFO iterator"""
        self.index = 0
        return self

    def __next__(self):
        """Return next value in LFO iterator, loops infinitely"""
        if self.index >= len(self.wavetable):
            self.index = 0
        val = self.wavetable[self.index]
        self.index += 1
        return val

    def __getitem__(self, i):
        """Return LFO value with index looping over"""
        if i >= len(self.wavetable):
            ncycles = i // len(self.wavetable)
            i -= int(ncycles * len(self.wavetable))
        return self.wavetable[i]

    def sine(self):
        """Initialize a sine wavetable containing one period"""
        n_points = int(1 / (self.frequency * self.step_size))
        self.wavetable = [(1 + math.sin(2 * math.pi * i / n_points)) / 2 for i in range(n_points)]

    def square(self):
        """Initialize a square wavetable containing one period"""
        n_points = int(1 / (self.frequency * self.step_size))
        half = int(n_points / 2)
        self.wavetable = [0 if i < half else 1 for i in range(n_points)]

    def triangle(self):
        """Initialize a triangle wave containing one period"""
        n_points = int(1 / (self.frequency * self.step_size))
        half = int(n_points / 2)
        step = 1 / half
        self.wavetable = [i * step if i < half else 1 - (i - half) * step for i in range(n_points)]
