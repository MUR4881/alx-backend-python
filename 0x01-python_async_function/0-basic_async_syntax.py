#!/usr/bin/env python3

# -*- encoding: utf-8 -*-
''' A simple module with a coroutine
'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''A simple coroutine that sleeps for a random time

    Args:
        max_delay: The maximum delay time that defaults to 0

    Returns:
        The float the randomly generated sleep_time

    '''

    sleep_time: float = random.uniform(0, max_delay)  #: the time to sleep
    await asyncio.sleep(sleep_time)
    return sleep_time
