from typing import Any, List

import pytest

from task3.combinations.combo import combinations_

combo1 = [[1, 3], [1, 4], [2, 3], [2, 4]]
combo2 = [
    [1, 3, 7],
    [1, 3, 8],
    [1, 4, 7],
    [1, 4, 8],
    [2, 3, 7],
    [2, 3, 8],
    [2, 4, 7],
    [2, 4, 8],
]
combo3 = [[1, 2]]
check1 = [1, 2], [3, 4]
check2 = [1, 2], [3, 4], [7, 8]
check3 = [1], [2]


# test for combinations/combo.py for funk combinations_()
@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (check1, combo1),
        (check2, combo2),
        (check3, combo3),
    ],
)
def test_combinations(value: List[Any], expected_result: List[List]):
    actual_result = combinations_(*value)

    assert actual_result == expected_result
