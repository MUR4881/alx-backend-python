#!/usr/bin/env python3

# -*- encoding: utf-8 -*-

""" A simple module containing a simple type annotated function
the function description/doc can be found in the function definition
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Generate a tuple of str, and int/float

    Args:
        k: The string
        v: The Float/int

    Return: tuple of the string and int/float
    """

    return (k, v**2)
