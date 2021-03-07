from typing import Any


def custom_range(line: Any, first: str, last: str = None, count: int = 1) -> list:
    """
    a function that takes any iteration of unique values
    and then it behaves like a range function
    """
    if last:
        lis = list(line[ord(first) - 97 : ord(last) - 97 : count])
    else:
        lis = list(line[ord("a") - 97 : ord(first) - 97 : count])
    return lis
