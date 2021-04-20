import pytest

from homework7.task1.tree.tree import find_occurrences

# Example trees:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}

example_tree_1 = {"key1": 1, "key2": {"key3": 2, "key4": 2, "key5": [1, 2, 3, 4, 5]}}

example_tree_2 = {("tt", "aa", "ss", "tt"): (1, {(1, 3): (2, 1)})}


# tests for tree/find_occurrences()
@pytest.mark.parametrize(
    ["tree", "element", "expected_result"],
    [
        (example_tree, "RED", 6),
    ],
)
def test_find_occurrences_with_example_tree_and_element_red(
    tree, element, expected_result
):
    actual_result = find_occurrences(tree, element)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["tree", "element", "expected_result"],
    [
        (example_tree, "BLUE", 2),
    ],
)
def test_find_occurrences_with_example_tree_and_element_blue(
    tree, element, expected_result
):
    actual_result = find_occurrences(tree, element)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["tree", "element", "expected_result"],
    [
        (example_tree_1, 1, 2),
    ],
)
def test_find_occurrences_with_example_tree_1_and_element_1(
    tree, element, expected_result
):
    actual_result = find_occurrences(tree, element)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["tree", "element", "expected_result"],
    [
        (example_tree_1, 2, 3),
    ],
)
def test_find_occurrences_with_example_tree_1_and_element_2(
    tree, element, expected_result
):
    actual_result = find_occurrences(tree, element)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["tree", "element", "expected_result"],
    [
        (example_tree_2, "tt", 2),
    ],
)
def test_find_occurrences_with_example_tree_2_and_element_tt(
    tree, element, expected_result
):
    actual_result = find_occurrences(tree, element)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["tree", "element", "expected_result"],
    [
        (example_tree_2, 1, 3),
    ],
)
def test_find_occurrences_with_example_tree_2_and_element_1(
    tree, element, expected_result
):
    actual_result = find_occurrences(tree, element)

    assert actual_result == expected_result
