from typing import Callable, OrderedDict


def cache(func: Callable) -> Callable:
    """
    a function that takes another function as an argument.
    then it returns a function like this.
    every function call is cached.
    """
    d = OrderedDict()  # dictionary for saving cache

    def inner(*args):
        if args in d:
            return d[args]
        else:
            m = func(*args)
            d[args] = m
            return m

    return inner
