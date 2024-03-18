#!/usr/bin/env python3
"""
Task 0: The basics of async.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    walts for a random delay between 0 and max delay.
    """
    a = random.uniform(0, max_delay)
    await asyncio.sleep(a)
    return a
