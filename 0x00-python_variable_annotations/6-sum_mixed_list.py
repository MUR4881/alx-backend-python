#!/usr/bin/env python3

# -*- encoding: utf-8 -*-

""" A simple module with a simple function using annotations
that is much of it, the function below is documented.

    Attributes:
        List (type): for type annotation of a function, list of integers
        and floats as parameter.
"""


from typing import List, Union  #: importing type annotation of list & Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums up a list of integers and / or floats

    Args:
        mxd_lst: The list of floats and/ or integers

    Returns: The sum as floats
    """

    total: float | int = 0  #: stores the sum of float list

    for num in mxd_lst:
        total += num

    return total
