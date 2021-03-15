import sys


def my_precious_logger(text: str):
    """
    a function that takes a string and writes it to stderr
    if the line starts with "error", otherwise before stdout.
    """
    if text[0:5] == "error":
        return print(text, file=sys.stderr)
    else:
        return print(text, file=sys.stdout)
