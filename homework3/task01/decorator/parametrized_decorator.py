"""
In previous homework task 4, you wrote a cache function that remembers other function output value. Modify it to be a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass
Would give out cached value up to times number only. Example:

@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead

>>> f()
? 1
'1'
>>> f()     # will remember previous value
'1'
>>> f()     # but use it up to two times only
'1'
>>> f()
? 2
'2'
"""


from typing import Callable


def cache(times: int = 1) -> Callable:
    """
    a parameterized decorator for caching functions that return values.
    :param times: the number of cached returns of the function.
    :return: function call value func.
    """

    def wrapper(func: Callable) -> Callable:
        diction = {}  # dictionary for saving cache

        def inner(*args):

            if (not diction) or (diction and diction[args][1] >= times):
                diction[args] = [func(*args), 0]
            else:
                diction[args][1] += 1
            return diction[args][0]

        return inner

    return wrapper
