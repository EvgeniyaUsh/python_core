"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>>> with suppressor(IndexError):
...    [][2]
>>> with Suppressor(IndexError):
...    [][2]
"""

from contextlib import AbstractContextManager, contextmanager


class Suppressor(AbstractContextManager):
    """
    The context manager that suppresses the passed exception,
    implemented as a class
    """

    def __init__(self, *exceptions):
        self._exceptions = exceptions

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type is not None and issubclass(exc_type, self._exceptions)


@contextmanager
def suppressor(*exceptions):
    """
    The context manager that suppresses the passed exception,
    implemented as a generator
    """
    try:
        yield
    except exceptions:
        pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
