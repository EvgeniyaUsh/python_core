from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    """
    A function that takes an element and finds the number of occurrences
    of this item in the tree.
    :param tree:
    :param element:
    :return: number of occurrences element in the tree.
    """
    counter = 0

    if isinstance(tree, dict):
        tree = tree.values()
    for key in tree:
        if not isinstance(key, (str, int)):
            counter += find_occurrences(key, element)
        elif key == element:
            counter += 1

    return counter
