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
    # delays = []
    # for f in asyncio.as_completed((eval("wait_random(max_delay), " * n))):
    #    delay = await f
    #    delays.append(delay)

    # Using comprehension form of the above
    return [await f for f in asyncio.as_completed(
        eval("wait_random(max_delay)," * n))]
