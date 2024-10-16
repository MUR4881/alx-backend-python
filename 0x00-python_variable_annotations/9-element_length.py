#!/usr/bin/env python3

# -*- encoding: utf-8 -*-


""" A simple module containing, a simple function that annotates (ducktyping)
"""

# Importing, Dependent typing
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Generates a List of Tuples of Sequence, and their length

    Args:
        lst: The iterable, containing Sequence

    Returns: The generated list
    """

    return [(i, len(i)) for i in lst]
