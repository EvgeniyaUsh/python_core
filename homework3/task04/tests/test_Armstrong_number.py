import pytest

from task04.Armstrong.Armstrong_number import is_armstrong


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (9, True),
        (10, False),
        (153, True),
    ],
)
def test_check_is_a_number_is_an_Armstrong_munber(value, expected_result):
    actual_result = is_armstrong(value)
    assert actual_result == expected_result
