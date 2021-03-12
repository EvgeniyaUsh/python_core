def is_armstrong(number: int) -> bool:
    degree = len(str(number))
    list_of_numbers = list(map(int, str(number)))
    numbers_to_degree = list(map(lambda x: x ** degree, list_of_numbers))
    return True if sum(numbers_to_degree) == number else False
