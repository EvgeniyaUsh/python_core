import pytest

from homework7.task2.hw2.hw2 import backspace_compare


# test for hw2/backspace_compare()
@pytest.mark.parametrize(
    ["value1", "value2", "expected_result"],
    [
        ("ab#c", "ad#c", True),
        ("a##c", "#a#c", True),
        ("a#c", "b", False),
    ],
)
def test_backspace_compare(value1: str, value2: str, expected_result: bool):
    actual_result = backspace_compare(value1, value2)

    assert actual_result == expected_result
