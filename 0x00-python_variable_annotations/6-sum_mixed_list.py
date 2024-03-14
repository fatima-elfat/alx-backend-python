#!/usr/bin/env python3
"""
Task 6 : Complex types - mixed list.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ takes a list mxd_lst of integers,
    Returns the sum as a float.
    """
    return float(sum(mxd_lst))
