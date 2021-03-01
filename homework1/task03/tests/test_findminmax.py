from typing import Tuple

import pytest

from task03.findminmax.fmm import find_maximum_and_minimum

file1 = "some_file1.txt"
file2 = "some_file2.txt"
file3 = "some_file3.txt"


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (file1, (1, 1)),
        (file2, (1, 5)),
        (file3, (-10, 98)),
    ],
)
def test_maximum_and_minimum(value: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result
