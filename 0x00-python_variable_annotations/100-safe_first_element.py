#!/usr/bin/env python3

# -*- encoding: utf-8 -*-

""" A simple module containing the annotations of a ducktyped function
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Retrieves the first element of the list

    Args:
        lst: The iterable of unknown type

    Returns: The first element of the list if possible, else None
    """
    if lst:
        return lst[0]
    else:
        return None
