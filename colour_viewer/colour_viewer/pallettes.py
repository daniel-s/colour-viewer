"""
@Author: Daniel Stojanov
2021-02-03
"""
import abc
import colorsys

class AbstractPallette(abc.ABC):
    @classmethod
    def get_no_of_fields(cls):
        return cls.__no_of_fields__
    @classmethod
    def get_label(cls):
        return cls.__name__.lower()
    @abc.abstractmethod
    def convert_colour(self):
        pass

class RGB(AbstractPallette):
    __no_of_fields__ = 3
    def convert_colour(parameters):
        """
        This is the simplest to convert to RGB, since
        we just forward the colours.
        """
        return list(parameters)

class HSV(AbstractPallette):
    __no_of_fields__ = 3
    def convert_colour(parameters):
        """
        This is the simplest to convert to RGB, since
        we just forward the colours.
        """
        values = colorsys.hsv_to_rgb(*parameters)
        return [value * 255 for value in values]

all_pallettes = [RGB, HSV]
