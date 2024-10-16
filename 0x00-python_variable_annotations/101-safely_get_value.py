#!/usr/bin/env python3

# -*- encoding: utf-8 -*-

""" A simple module containing a simple function with complex
Type Annotations.
"""

from typing import Union, Any, Mapping, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Get a value from a mapping safely

    Args:
        dct: The mapping, e.g Dictionary.
        key: The key, to index the mappy with
        default: The default to be returned, if key doesn't exist in dct

    Return: The value(mapped to) or default
    """

    if key in dct:
        return dct[key]
    else:
        return default
