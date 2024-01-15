#!/usr/bin/env python3
"""
Module 1-concurrent_coroutines
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay
    return the list of all the delays (float values)
    """
    result = []
    aws = [wait_random(max_delay) for i in range(n)]
    for t in asyncio.as_completed(aws):
        result.append(await t)
    return result
