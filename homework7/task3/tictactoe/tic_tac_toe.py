"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from itertools import chain
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    list_board = list(chain(*board))
    winner = check_diagonal_win(list_board)
    if winner:
        return f"{winner} wins!"
    winner = check_rows_win(board)
    if winner:
        return f"{winner} wins!"
    elif "-" in board[0] or "-" in board[1] or "-" in board[2]:
        return "unfinished"
    else:
        return "draw!"


def check_diagonal_win(list_board: List):
    """
    a function that looks for a winner diagonally
    :param list_board:
    :return: winner if any, otherwise None
    """
    if (
        list_board[::4].count(list_board[0]) == 3
        or list_board[2:7:2].count(list_board[2]) == 3
    ):
        return list_board[4]
    return None


def check_rows_win(board: List[List]):
    """
    a function that searches for a winner line by line
    :param board:
    :return: winner if any, otherwise None
    """
    for row in board:
        if "-" not in row and len(set(row)) == 1:
            return row[0]
    return None
