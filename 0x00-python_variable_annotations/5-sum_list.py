#!/usr/bin/env python3
"""
Task 5: Complex types - list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ takes a list input_list of floats,
    Returns the addition of the values of the input list.
    """
    return float(sum(input_list))
