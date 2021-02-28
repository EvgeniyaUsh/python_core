from collections.abc import Sequence


def _check_window(x: int, y: int, z: int) -> bool:
    return (x + y) == z


data_to_process = [0,1,1,2]

# assert len(data_to_process) >= 3

# a, b, c = data_to_process[0], data_to_process[1], data_to_process[2]

"""while data_to_process:
    print(a, b, c)
    if not _check_window(a, b, c):
        print(a, b, c)
        raise ValueError("Invalid data")

    data_to_process = data_to_process[1:]
    a, b, c = b, c, data_to_process[2]

print("it's a fib sequence!")"""


def check_fibonacci(data: Sequence[int]) -> bool:
    assert len(data_to_process) >= 3, "it's not a fib sequence!"
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
            print(a, b, c)
    return True


print(check_fibonacci(data_to_process))
