import io

from homework3.task01.decorator.parametrized_decorator import cache


@cache(times=2)
def func() -> str:
    return input("? ")


# test for decorator/parametrized_decorator.py for decorator @cache
def test_func_cached_2_times(monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO("str1"))
    actual_result1 = func()
    actual_result2 = func()
    actual_result3 = func()

    monkeypatch.setattr("sys.stdin", io.StringIO("str1"))
    actual_result4 = func()
    assert actual_result1 is actual_result2 is actual_result3 is not actual_result4
