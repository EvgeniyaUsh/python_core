from functools import lru_cache
from typing import Callable


def cache(func: Callable) -> Callable:
    """
    a function that takes another function as an argument.
    then it returns a function like this.
    every function call is cached.
    """

    @lru_cache
    def inner(*args):
        return func(*args)

    return inner
