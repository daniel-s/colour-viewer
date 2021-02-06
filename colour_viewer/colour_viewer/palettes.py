"""
@Author: Daniel Stojanov
2021-02-03
"""
import abc
import colorsys

class AbstractPalette(abc.ABC):
    @classmethod
    def get_no_of_fields(cls):
        return cls.__no_of_fields__
    @classmethod
    def get_label(cls):
        return cls.__name__.lower()
    @abc.abstractmethod
    def convert_colour(self):
        pass

class RGB(AbstractPalette):
    __no_of_fields__ = 3
    def convert_colour(parameters):
        """
        This is the simplest to convert to RGB, since
        we just forward the colours.
        """
        return list(parameters)

class HSV(AbstractPalette):
    __no_of_fields__ = 3
    def convert_colour(parameters):
        values = colorsys.hsv_to_rgb(*parameters)
        return [value * 255 for value in values]

class BRGB(AbstractPalette):
    __no_of_fields__ = 3
    def convert_colour(parameters):
        multiplier = (255 / 10000)
        return [value * multiplier for value in parameters]

all_palettes = [RGB, HSV, BRGB]
