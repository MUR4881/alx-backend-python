#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
Contains function to measure the time taken
by a coroutine wait_n that also relies on
random_wait, which waites for random amount of time
'''

import time
import asyncio
from typing import Callable
wait_n: Callable = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Measure runtime/perfomance of the function
    wait_n(n, max_delay)

    Args: arguments to wait_n
        n: the number of times wait_random is called
        by wait_n.
        max_delay: the max delay from wait_random

    Returns:
        the average time of each call to wait_random
    '''

    time_started: float = time.perf_counter()  # time started
    asyncio.run(wait_n(n, max_delay))
    time_taken: float = time.perf_counter() - time_started  # perfomance !

    return time_taken / n  # Average time per wait_random
