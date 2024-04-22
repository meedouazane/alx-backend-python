#!/usr/bin/env python3
"""Tasks"""
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays """
    lst = []
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        lst.append(delay)
        lst.sort()
    return lst
