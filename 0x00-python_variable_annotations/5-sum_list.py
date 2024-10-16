#!/usr/bin/env python3

# -*- encoding: utf-8 -*-

""" A simple module with a simple function using annotations
that is much of it, the function below is documented.

    Attributes:
        List (type): for type annotation of a function, list of float
        as param.
"""


from typing import List  #: importing type annotation of list


def sum_list(input_list: List[float]) -> float:
    """Sums up a list of floats

    Args:
        input_list: The list of floats

    Returns: The sum of the floats
    """

    total: float = 0  #: stores the sum of float list

    for num in input_list:
        total += num

    return total
