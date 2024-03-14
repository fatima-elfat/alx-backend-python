#!/usr/bin/env python3
"""
Task 7: Complex types - string and int/float to tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    takes a two elements, The first element of the tuple is the string k.
    The second element is the square of the int/float v
    and should be annotated as a float.
    Returns a tuple.
    """
    return (k, v**2)
