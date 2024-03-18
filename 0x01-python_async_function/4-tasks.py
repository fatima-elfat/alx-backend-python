#!/usr/bin/env python3
"""
Task 4: Tasks.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ spawns task_wait_random n times with the specified max_delay..
    Returns: the list of all the delays.
    """
    ts = [task_wait_random(max_delay) for i in range(n)]
    res = [await t for t in asyncio.as_completed(ts)]
    return res
