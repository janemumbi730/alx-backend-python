#!/usr/bin/env python3
"""Implement measure_runtime"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure total runtime"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension()for i in range(4)))
    ends = time.perf_counter()
    return (ends - start)
