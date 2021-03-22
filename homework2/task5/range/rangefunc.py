from typing import Any, List


def custom_range(line: Any, *args: Any) -> List:
    """
    a function that takes any iteration of unique values
    and then it behaves like a range function
    """
    first, last, count = 0, len(line), 1
    if len(args) == 1:
        last = line.index(args[0])
    else:
        if len(args) == 3:
            count = args[2]
        first = line.index(args[0])
        last = line.index(args[1])

    return list(line[first:last:count])
