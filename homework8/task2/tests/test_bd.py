import pytest

from homework8.task2.bd_sqlite.bd import TableData

presidents = TableData(data_base="example.sqlite", table_name="presidents")


# tests for bd/TableData class
@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("Yeltsin", ("Yeltsin", 999, "Russia")),
        ("Trump", ("Trump", 1337, "US")),
    ],
)
def test_class_table_data_method_getitem_with_value_yeltsin_and_trump(
    value, expected_result
):
    actual_result = presidents[value]
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("Trump", True),
        ("Yeltsin", True),
        ("Big Man Tyrone", True),
    ],
)
def test_class_table_data_method_contains_true(value, expected_result):
    actual_result = value in presidents
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("Jonson", False),
        ("Abama", False),
    ],
)
def test_class_table_data_method_contains_false(value, expected_result):
    actual_result = value in presidents
    assert actual_result == expected_result


def test_class_table_data_method_len():
    assert len(presidents) == 3


def test_class_table_data_method_iter():
    pr = []
    for president in presidents:
        pr.append(president[0])
    assert pr == ["Big Man Tyrone", "Trump", "Yeltsin"]
