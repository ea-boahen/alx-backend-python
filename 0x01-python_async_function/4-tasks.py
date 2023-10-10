#!/usr/bin/env python3
""" Tasks """
import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').wait_random

async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
        Args:
            max_delay: max wait
            n: spawn function

        Return:
            multiples tasks
    """
    delays: List[float] = []
    tasks: List[asyncio.Task] = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for n in asyncio.as_completed((tasks)):
        delay = await n
        delays.append(delay)

    return delays
