import pytest

from task02.slow_calc.calc import slow_calculate, sum_of_slow_calculations


# test for slow_calc/calc.py for funk slow_calculate()
@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (0, 2785),
        ("Hello", 2023),
        (-3, 2193),
        (88, 1722),
        (None, 2056),
    ],
)
def test_slow_calculate(value, expected_result):
    actual_result = slow_calculate(value)
    assert actual_result == expected_result


# test for slow_calc/calc.py for funk sum_of_slow_calculations()
@pytest.mark.parametrize(
    ["expected_result"],
    [[1024259]],
)
def test_sum_of_slow_calculations(expected_result):
    actual_result = sum_of_slow_calculations()
    assert actual_result == expected_result
