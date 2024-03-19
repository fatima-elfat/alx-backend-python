#!/usr/bin/env python3
"""
Task 0: Async Generator.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    loops 10 times, each time asynchronously wait 1 second,
    then yield a random.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random()
