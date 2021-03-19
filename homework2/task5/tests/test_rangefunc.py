import string
from typing import Any, List

import pytest

from homework2.task5.range.rangefunc import custom_range


# test for range/rangefunc.py for funk custom_range()
@pytest.mark.parametrize(
    ["line", "args", "expected_result"],
    [
        (string.ascii_lowercase, "g", ["a", "b", "c", "d", "e", "f"]),
        (
            string.ascii_lowercase,
            ["g", "p"],
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        (string.ascii_lowercase, ["p", "g", -2], ["p", "n", "l", "j", "h"]),
    ],
)
def test_range(line: Any, args, expected_result: List):
    actual_result = custom_range(line, *args)
    assert actual_result == expected_result
