from typing import List

import pytest
from task05.subarray.sumsubarray import find_maximal_subarray_sum


# test for subarray/sumsubarray.py
@pytest.mark.parametrize(
    ["value", "k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([1, 2, 445, 5, 2, 87], 2, 450),
        ([1, 2, 3, 4, 5], 0, 0),
        ([1, 2, 3, 4, 5], 1, 5),
    ],
)
def test_maximum_and_minimum(value: List[int], k: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(value, k)

    assert actual_result == expected_result
