#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays """
    lst = []
    lstOrderd = []
    for _ in range(n):
        delay = wait_random(max_delay)
        lst.append(delay)
    for i asyncio.as_completed(lst):
        lstOrderd.append(await i)
    return lstOrderd
