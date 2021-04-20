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
        tree_keys = tree.keys()
        tree = tree.values()
        for key in tree_keys:
            counter = count_counter(key, element, counter)

    for key in tree:
        counter = count_counter(key, element, counter)

    return counter


def count_counter(key, element, counter):
    if not isinstance(key, (str, int)):
        counter += find_occurrences(key, element)
    elif key == element:
        counter += 1
    return counter
