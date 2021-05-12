import pytest

from homework11.task2.strategy_pattern.strategy_pattern import Order, MorningDiscount, ElderDiscount


# tests for strategy_pattern/Order, MorningDiscount, ElderDiscount classes
@pytest.mark.parametrize(
    ["value", "func", "expected_result"],
    [
        (100, MorningDiscount, 50),
    ],
)
def test_strategy_pattern_morning_discount_with_anticipation_50(value, func, expected_result):
    actual_result = Order(value, func).final_price()
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "func", "expected_result"],
    [
        (100, ElderDiscount, 10),
    ],
)
def test_strategy_pattern_morning_discount_with_anticipation_10(value, func, expected_result):
    actual_result = Order(value, func).final_price()
    assert actual_result == expected_result
