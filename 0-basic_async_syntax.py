#!/usr/bin/env python3
"""Module 0-basic_async_syntax"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine that takes in an integer argument"""
    rand_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(rand_delay)
    return rand_delay
