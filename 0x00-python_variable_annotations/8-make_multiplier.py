#!/usr/bin/env python3

# -*- encoding: utf-8 -*-

""" A simple module containing a simple function with complex
annotations!
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Generate a function that multplier a float with
    multiplier

    Args:
        multiplier (float): The float, to multiplier the new function
        float with.

    Returns: a function that multiplies it arg, with multiplier
    """

    def Multiplier(n: float) -> float:
        """Multiplier n, with a variable in it lexical scope

        Args:
            n: the float to be multiplied by the multiplier

        Returns: multiplier * n -> multiplier, from closure, lexical scoping!
        """

        return n * multiplier

    return Multiplier
