#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
Run a coroutine multiple times to test for
concurrency
'''
import asyncio
from typing import Sequence, Callable
wait_random: Callable = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> Sequence[float]:
    '''spawns wait_random n times

    Args:
        n: The number of times to spawn wait_random
        max_delay: maximum sleep time of wait_random (non_blocking)

    Returns: a list of wait time(s) {delay}
    '''

    calls = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return calls
