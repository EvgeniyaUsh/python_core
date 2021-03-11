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
