import pytest

from task03.helper_filter.help_filter import Filter, make_filter

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
    10,
    12,
    14,
    16,
    18,
    20,
    22,
    24,
    26,
    28,
    30,
    32,
    34,
    36,
    38,
    40,
    42,
    44,
    46,
    48,
    50,
    52,
    54,
    56,
    58,
    60,
    62,
    64,
    66,
    68,
    70,
    72,
    74,
    76,
    78,
    80,
    82,
    84,
    86,
    88,
    90,
    92,
    94,
    96,
    98,
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
    actual_result = value.apply(range(100))
    assert actual_result == expected_result
