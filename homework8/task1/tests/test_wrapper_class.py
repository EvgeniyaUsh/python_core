import pytest

from homework8.task1.wrapper_class.wrapper_class import KeyValueStorage

test_class = KeyValueStorage("file_path.txt")


# tests for wrapper_class/KeyValueStorage class
@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("name", "kek"),
    ],
)
def test_class_key_value_storage_like_dict_with_value_name(value, expected_result):
    actual_result = test_class[value]
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("last_name", "top"),
    ],
)
def test_class_key_value_storage_like_dict_with_value_last_name(value, expected_result):
    actual_result = test_class[value]
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("song", "shadilay"),
    ],
)
def test_class_key_value_storage_like_dict_with_value_song_name(value, expected_result):
    actual_result = test_class[value]
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("power", 9001),
    ],
)
def test_class_key_value_storage_like_dict_with_value_power(value, expected_result):
    actual_result = test_class[value]
    assert actual_result == expected_result


def test_class_key_value_storage_like_attributes_with_name():
    assert test_class.name == "kek"


def test_class_key_value_storage_like_attributes_with_last_name():
    assert test_class.last_name == "top"


def test_class_key_value_storage_like_attributes_with_song_name():
    assert test_class.song == "shadilay"


def test_class_key_value_storage_like_attributes_with_power():
    assert test_class.power == 9001
