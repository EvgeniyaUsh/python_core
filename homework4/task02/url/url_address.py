import requests


def count_dots_on_i(url: str) -> int:
    """
    a function that takes a url as input
    and counts how many letters `i` are present in the HTML at this URL.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            counter = response.text.count("i")
    except Exception:
        raise ValueError(f"Unreachable {url}")
    return counter
