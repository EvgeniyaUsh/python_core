import math
from collections.abc import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """
    A function that returns True if the sequence is a Fibonacci sequence, and vice versa.
    Written using Binet's formula
    """
    length = len(data)
    SQRT5 = math.sqrt(5)
    PHI = (SQRT5 + 1) / 2  # the "golden ratio" is calculated
    count = 0
    if length < 3:
        return False
    for i in range(length):
        # the numbers from the 'data' are compared with the corresponding elements
        # from the fibonacci list
        if data[i] == int(PHI ** i / SQRT5 + 0.5):
            count += 1
    if length == count:
        return True
    else:
        return False
