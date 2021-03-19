import pytest

from homework3.task03.helper_filter.help_filter import Filter, make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]

positive_even = Filter(
    lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)
)

even_nums = [
    2,
    4,
    6,
    8,
]


# test for helper_filter/help_filter.py
@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ({"name": "polly", "type": "bird"}, [sample_data[1]]),
    ],
)
def test_help_filter_that_generates_data_filtering_object_from_a_list_of_keyword_parameters_1(
    value, expected_result
):
    actual_result = make_filter(**value).apply(sample_data)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (positive_even, even_nums),
    ],
)
def test_help_filter_that_generates_data_filtering_object_from_a_list_of_keyword_parameters_2(
    value, expected_result
):
    actual_result = value.apply(range(10))
    assert actual_result == expected_result
