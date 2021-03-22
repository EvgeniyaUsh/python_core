import numpy as np


def fizzbuzz(n):
    """
    FizzBuzz on numpy.
    :param n: the number of numbers in the list
    :return: "Fizz" if the number is divisible by three,
    "Buzz" if the number is divisible by five,
    "Fizz Buzz" if the number is divisible by,
     otherwise the numbers do not change.

    >>> fizzbuzz(5)
    [1, 2, 'Fizz', 4, 'Buzz']
    >>> fizzbuzz(16)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz', 16]
    >>> fizzbuzz("string")
    Traceback (most recent call last):
        ...
    ValueError
    """
    try:
        fb = np.arange(n + 1, dtype="object")
        fb[::3] = "Fizz"
        fb[::5] = "Buzz"
        fb[::15] = "Fizz Buzz"
    except Exception:
        raise ValueError
    return list(fb[1:])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
