from typing import Callable

import pytest

from homework2.task4.decorator.decor import cache


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200
some1 = 5, 2
val = cache_func(*some)
val_1 = cache_func(*some1)


# test for decorator/decor.py for decorator cache
@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (some, val),
        (some1, val_1),
    ],
)
def test_combinations(value: Callable, expected_result: Callable):
    actual_result = cache_func(*value)

    assert actual_result == expected_result
