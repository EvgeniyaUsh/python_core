def is_armstrong(number: int) -> bool:
    """
    a function in functional style that determines whether a number is an Armstrong number.
    :param number:
    :return: True if yes and vice versa
    """
    degree = len(str(number))
    result = sum(int(num) ** degree for num in str(number))
    return result == number
