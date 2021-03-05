from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """
    a function that reads input data line by line and finds the maximum and minimum values.
    """
    mass = []
    with open(file_name) as fi:
        for line in fi:
            mass.append(int(line))
    min_max_tuple = (min(mass), max(mass))
    return min_max_tuple
