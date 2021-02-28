def check_power_of_2(a: int) -> bool:
    if a == 0:
        return bool(a & (a - 1))
    return not (bool(a & (a - 1)))
