from itertools import product
from typing import Any, List


def combinations_(*args: List[Any]) -> List[List]:
    """
    the function takes K lists as arguments and returns all possible
    lists of K elements, where the first element is from the first list,
    the second from the second and so one.
    """
    combo = []
    k = list(product(*args))
    for i in k:
        combo.append(list(i))
    return combo
