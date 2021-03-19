import pytest

from homework3.task04.Armstrong.Armstrong_numbers import is_armstrong


# test for Armstrong/Armstrong_numbers.py for funk is_armstrong()
@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (9, True),
        (10, False),
        (153, True),
        (0, True),
    ],
)
def test_check_if_a_number_is_an_armstrong_number(value, expected_result):
    actual_result = is_armstrong(value)
    assert actual_result == expected_result
