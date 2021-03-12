def is_armstrong(number: int) -> bool:
    """
    a function in functional style that determines whether a number is an Armstrong number.
    :param number:
    :return: True if yes and vice versa
    """
    degree = len(str(number))
    list_of_numbers = list(map(int, str(number)))
    numbers_to_degree = list(map(lambda x: x ** degree, list_of_numbers))
    return True if sum(numbers_to_degree) == number else False
