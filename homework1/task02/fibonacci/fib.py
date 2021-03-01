from collections.abc import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) < 3:
        return False
    a, b, c = data[0], data[1], data[2]
    while len(data):
        if a + b != c:
            return False
        elif len(data) == 3:
            a, b, c = data[0], data[1], data[2]
            return a + b == c
        else:
            data = data[1:]
            a, b, c = b, c, data[2]
    return True