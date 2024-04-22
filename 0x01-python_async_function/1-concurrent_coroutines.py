#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """return the list of all the delays """
    lst = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        lst.append(delay)
        lst.sort()
    return lst
