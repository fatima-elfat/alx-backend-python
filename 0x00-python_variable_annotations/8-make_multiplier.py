#!/usr/bin/env python3
"""
Task 8 :  Complex types - functions.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument,
    Returns a function that multiplies a float by multiplier.
    """
    return lambda a: a * multiplier
