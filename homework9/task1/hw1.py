from contextlib import ExitStack
from itertools import chain
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """
    >>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
    [1, 2, 3, 4, 5, 6]

    >>> list(merge_sorted_files(["file1.txt", "file2.txt", "file3.txt"]))
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    with ExitStack() as stack:
        streams = (stack.enter_context(open(fname)) for fname in file_list)
        contents = [f.read().split() for f in streams]
        return merge_sorted_iterables(contents)


def merge_sorted_iterables(iters):
    flat_list = list(chain(*iters))
    sorted_int_list = sorted(int(item) for item in flat_list)
    yield from sorted_int_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
