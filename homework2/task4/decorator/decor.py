from typing import Callable


def cache(func: Callable) -> Callable:
    """
    a function that takes another function as an argument.
    then it returns a function like this.
    every function call is cached.
    """
    cached = dict()  # dictionary for saving cache

    def inner(*args):
        if args in cached:
            return cached[args]
        else:
            m = func(*args)
            cached[args] = m
            return m

    return inner
