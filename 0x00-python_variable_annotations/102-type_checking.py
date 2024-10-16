#!/usr/bin/env python3

# -*- encoding: utf-8 -*-

""" A simple module, containing , nothing but a simple function with
complex type annotations!
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Zooms an array, increase the number of occurence for each element

    Args:
        lst: A tuple of the elements/entry
        factor: The Scale factor the number of times, all should appear

    Return:
        A list of the magnified Array
    """

    zoomed_in: List = [
            item for item in lst
            for i in range(factor)
            ]
    return zoomed_in


array = (12, 72, 91)  #: Tuple: An array to be zoomed

zoom_2x = zoom_array(array)  #: List: array zoomed twice
zoom_3x = zoom_array(array, 3)  #: List: array zoomed 3x
