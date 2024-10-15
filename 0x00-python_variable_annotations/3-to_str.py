#!/usr/bin/env python3

# -*- encoding: utf-8 -*-

""" A simple module with a simple function with type annotations
"""


def to_str(n: float) -> str:
    """ converts a float to a string representation

    Args:
        n: a float as argument

    Returns: A string representation of the float
    """

    return n.__str__()
