#!/usr/bin/env python3
"""
Task 1: Let's execute multiple coroutines
at the same time with async.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ spawns wait_random n times with the specified max_delay..
    Returns: the list of all the delays.
    """
    ts = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    res = [await t for t in asyncio.as_completed(ts)]
    return res
