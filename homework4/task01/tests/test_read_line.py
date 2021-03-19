import os

import pytest

from homework4.task01.read_files.read_file import read_magic_number


# tests for read_files/read_file.py for funk read_magic_number()
@pytest.mark.parametrize(
    "value",
    [
        "1",
        "0",
        "2",
        "1.2",
        "2.9",
    ],
)
# interval [1, 3)
def test_read_magic_number_for_numbers_in_the_interval(value: str):
    with open("text.txt", "w") as file:
        file.write(value)
    assert read_magic_number("text.txt") is True
    os.remove("text.txt")


@pytest.mark.parametrize(
    "value",
    [
        "3",
        "-1",
        "10",
        "-8",
    ],
)
# interval [1, 3)
def test_read_magic_number_for_numbers_not_in_the_interval(value: str):
    with open("text.txt", "w") as file:
        file.write(value)
    assert read_magic_number("text.txt") is False
    os.remove("text.txt")


@pytest.mark.parametrize(
    "value",
    [
        "hello",
    ],
)
def test_read_magic_number_for_case_that_raises_value_error(value: str):
    with open("text.txt", "w") as file:
        file.write(value)
        with pytest.raises(ValueError):
            read_magic_number("text.txt")
    os.remove("text.txt")
