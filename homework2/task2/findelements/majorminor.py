from collections import Counter
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """
    the function finds the most common and least common elements in an array
    """
    new_list = Counter(inp)
    tup = new_list.most_common()[0][0], new_list.most_common()[-1][0]
    return tup
