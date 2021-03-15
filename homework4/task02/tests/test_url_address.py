import pytest

from task02.url.url_address import count_dots_on_i


# tests for url/url_address.py for funk count_dots_on_i()
@pytest.mark.parametrize(
    ["value", "expected"],
    [
        ("https://example.com/", 59),
        ("https://pythontutor.ru/", 979),
    ],
)
def test_count_i_in_the_html_code_of_the_site_page(value: str, expected: int):
    assert count_dots_on_i(value) == expected


@pytest.mark.parametrize(
    "link",
    ["https://exampleerror.com/", "https://pythontutorerror.ru/"],
)
def test_takes_a_broken_links_and_raises_value_error(link: str):
    with pytest.raises(ValueError) as e:
        assert count_dots_on_i(link)
    assert str(e.value) == f"Unreachable {link}"
