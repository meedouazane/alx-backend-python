#!/usr/bin/env python3
"""Tasks"""
from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays """
    lst = []
    lstOrderd = []
    for _ in range(n):
        delay = task_wait_random(max_delay)
        lst.append(delay)
    for i in asyncio.as_completed(lst):
        lstOrderd.append(await i)
    return lstOrderd
