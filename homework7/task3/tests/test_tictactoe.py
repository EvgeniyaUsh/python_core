from typing import List

import pytest

from homework7.task3.tictactoe.tic_tac_toe import tic_tac_toe_checker

game1 = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]

game2 = [["x", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]

game3 = [["x", "-", "o"], ["-", "x", "o"], ["x", "-", "o"]]

game4 = [["x", "o", "x"], ["o", "o", "x"], ["x", "x", "o"]]


# test for tic_tac_toe/tic_tac_toe_checker()
@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (game1, "unfinished"),
    ],
)
def test_tic_tac_toe_checker_when_unfinished(value: List[List], expected_result: str):
    actual_result = tic_tac_toe_checker(value)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (game2, "x wins!"),
    ],
)
def test_tic_tac_toe_checker_when_x_wins(value: List[List], expected_result: str):
    actual_result = tic_tac_toe_checker(value)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (game3, "o wins!"),
    ],
)
def test_tic_tac_toe_checker_when_o_wins(value: List[List], expected_result: str):
    actual_result = tic_tac_toe_checker(value)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (game4, "draw!"),
    ],
)
def test_tic_tac_toe_checker_when_o_wins(value: List[List], expected_result: str):
    actual_result = tic_tac_toe_checker(value)
    assert actual_result == expected_result
