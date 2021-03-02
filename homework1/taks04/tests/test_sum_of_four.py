from typing import List

import pytest

from taks04.sum_of_four.walnut import check_sum_of_four


@pytest.mark.parametrize(
    ["a", "b", "c", "d", "expected_result"],
    [
        ([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 81),
        ([2, 1, 1], [3, 4, 2], [8, 2, 6], [3, 8, 4], 0),
        ([-2, 1], [-3, 4], [8, 2], [3, 8], 1),
    ],
)
def test_sum_of_four(
    a: List[int], b: List[int], c: List[int], d: List[int], expected_result: int
):
    actual_result = check_sum_of_four(a, b, c, d)

    assert actual_result == expected_result
