#!/usr/bin/env python3
"""
Task 11 : More involved type annotations.
"""
from typing import Any, Mapping, Union, TypeVar


"""using the hint"""
T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
     ) -> Union[Any, T]:
    """
    gets value safly.
    Return value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
