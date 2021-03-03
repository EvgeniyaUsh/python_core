def check_power_of_2(a: int) -> bool:
    """
    a function that checks if a number is a power of two
    """
    return bool(a and (a & (a - 1)) == 0)
