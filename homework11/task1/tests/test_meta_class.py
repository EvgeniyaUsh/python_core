import pytest

from homework11.task1.meta_class.meta_class import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


def test_class_colors_enum_red():
    assert ColorsEnum.RED == "RED"


def test_class_colors_enum_black():
    assert ColorsEnum.BLACK == "BLACK"


def test_class_size_enum_xl():
    assert SizesEnum.XL == "XL"


def test_class_size_enum_m():
    assert SizesEnum.M == "M"


def test_key_error_colors_enum():
    with pytest.raises(KeyError):
        ColorsEnum.BROWN


def test_key_error_sizes_enum():
    with pytest.raises(KeyError):
        ColorsEnum.XXL
