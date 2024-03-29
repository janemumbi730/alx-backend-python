#!/usr/bin/env python3
"""
Module 0-async_generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    The coroutine will loop 10 times, each time asynchronously
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
