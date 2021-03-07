import string
from typing import Any

import pytest

from task5.range.rangefunc import custom_range


# test for range/rangefunc.py for funk custom_range()
@pytest.mark.parametrize(
    ["line", "first", "last", "count", "expected_result"],
    [
        (string.ascii_lowercase, "p", "g", -2, ["p", "n", "l", "j", "h"]),
        (string.ascii_lowercase, "g", None, 1, ["a", "b", "c", "d", "e", "f"]),
        (
            string.ascii_lowercase,
            "g",
            "p",
            1,
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
    ],
)
def test_range(line: Any, first: str, last: str, count: int, expected_result: list):
    actual_result = custom_range(line, first, last, count)

    assert actual_result == expected_result
