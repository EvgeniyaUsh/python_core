from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    a function that takes an N number as input and returns N FizzBuzzaaa numbers.
    :param n: the number of numbers in the list
    :return: 'fizz' if the number is divisible by three,
    'buzz' if the number is divisible by five,
    otherwise the numbers do not change.

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz(16)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizz buzz', '16']
    >>> fizzbuzz("string")
    Traceback (most recent call last):
        ...
    ValueError
    """
    fizzbuzz_nums = []
    try:
        for i in range(1, n + 1):
            if i % 15 == 0:
                i = "fizz buzz"
            elif i % 5 == 0:
                i = "buzz"
            elif i % 3 == 0:
                i = "fizz"
            fizzbuzz_nums.append(str(i))
    except Exception:
        raise ValueError
    return fizzbuzz_nums


if __name__ == "__main__":
    import doctest

    doctest.testmod()
