#!/usr/bin/env python3
"""
Task 2: Run time for four parallel comprehensions.
"""
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    execute async_comprehension four
    times in parallel using asyncio.gather.
    """
    r1 = time()
    ts = [async_comprehension() for i in range(4)]
    await asyncio.gather(*ts)
    r2 = time()
    return (r2 - r1)

async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)
