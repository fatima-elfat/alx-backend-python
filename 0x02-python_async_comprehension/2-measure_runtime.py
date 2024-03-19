#!/usr/bin/env python3
"""
Task 2: Run time for four parallel comprehensions.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    execute async_comprehension four
    times in parallel using asyncio.gather.
    """
    r1 = time.perf_counter()
    ts = [async_comprehension() for i in range(4)]
    await asyncio.gather(*ts)
    r2 = time.perf_counter()
    return (r2 - r1)

async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)
