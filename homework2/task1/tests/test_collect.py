from typing import List

import pytest

from homework2.task1.work_with_text.collect import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)

data = "data.txt"
mass = [
    "Verfassungsverletzungen",
    "Wiederbelebungsübungen",
    "Werkstättenlandschaft",
    "Geschichtsphilosophie",
    "Werkstättenlandschaft",
    "Entscheidungsschlacht",
    "Selbstbezichtigungen",
    "Geschichtsunterricht",
    "Gewissenserforschung",
    "menschenfreundlichen",
]


# test for work_with_text/collect.py for funk get_longest_diverse_words()
@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (data, mass),
    ],
)
def test_longest_diverse_words(file_path: str, expected_result: List[str]):
    actual_result = get_longest_diverse_words(file_path)

    assert actual_result == expected_result


# test for work_with_text/collect.py for funk get_rarest_char()
@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (data, ")"),
    ],
)
def test_rarest_char(file_path: str, expected_result: str):
    actual_result = get_rarest_char(file_path)

    assert actual_result == expected_result


# test for work_with_text/collect.py for funk count_punctuation_chars()
@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (data, 5305),
    ],
)
def test_punctuation_chars(file_path: str, expected_result: int):
    actual_result = count_punctuation_chars(file_path)

    assert actual_result == expected_result


# test for work_with_text/collect.py for funk count_non_ascii_chars()
@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (data, 2972),
    ],
)
def test_non_ascii_chars(file_path: str, expected_result: int):
    actual_result = count_non_ascii_chars(file_path)

    assert actual_result == expected_result


# test for work_with_text/collect.py for funk get_most_common_non_ascii_char()
@pytest.mark.parametrize(
    ["file_path", "expected_result"],
    [
        (data, "äüßö"),
    ],
)
def test_most_common_non_ascii_char(file_path: str, expected_result: str):
    actual_result = get_most_common_non_ascii_char(file_path)

    assert actual_result == expected_result
