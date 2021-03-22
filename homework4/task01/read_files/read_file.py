import os


def read_magic_number(path: str) -> bool:
    """
    a function that gets file path as an argument and read the first line of the file.
    Throws ValueError if any error occurs.
    :param path: file path
    :return: true if the number is in the interval [1, 3) and false otherwise
    """
    if os.path.exists(path):
        try:
            with open(path) as f:
                first_line = float(f.readline().strip())
        except Exception:
            raise ValueError from None
        else:
            return 0 <= first_line < 3
    else:
        raise ValueError
