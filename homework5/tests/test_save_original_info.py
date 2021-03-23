import pytest

from homework5.decorator.save_original_info import custom_sum, print_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (([1, 2, 3], [4, 5]), [1, 2, 3, 4, 5]),
        ((1, 2, 3, 4), 10),
    ],
)
def test_custom_sum_decorated(value, expected_result):
    custom_sum_new = print_result(custom_sum)
    actual_result = custom_sum_new(*value)
    assert actual_result == expected_result


def test_check_my_wraps_doc():
    assert custom_sum.__doc__ == print_result(custom_sum).__doc__


def test_check_my_wraps_name():
    assert custom_sum.__name__ == print_result(custom_sum).__name__


def test_check_my_wraps_original_func():
    assert print_result(custom_sum).__original_func == custom_sum
