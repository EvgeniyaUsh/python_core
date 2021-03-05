import re
import string
from collections import Counter
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    the function finds the 10 longest words with the most unique characters
    """
    mass = []
    with open(file_path, "rb") as f:
        data = f.read().decode("unicode-escape")
        data1 = re.findall(r"[\w']+|[set(string.punctuation)]", data)
        c = 1
        for i in data1:
            if len(set(i)) >= len(set(data1[c])):
                mass.append(i)
            c += 1
            if c == len(data1):
                break
    return sorted(mass, key=lambda w: len(w), reverse=True)[:10]


def get_rarest_char(file_path: str) -> str:
    """
    function to find the rarest symbol for a document
    """
    with open(file_path, "rb") as f:
        data = f.read().decode("unicode-escape")
        counts = Counter(data).most_common()
        return counts[-1][0]


def count_punctuation_chars(file_path: str) -> int:
    """
    the function counts all punctuation marks in the text
    """
    count = 0
    with open(file_path, "rb") as f:
        data = f.read().decode("unicode-escape")
        counts = Counter(data)
        for key, item in counts.items():
            if key in set(string.punctuation):
                count += item
    return count


def count_non_ascii_chars(file_path: str) -> int:
    """
    the function counts the number of all non-ascii characters in the text
    """
    count = 0
    with open(file_path, "rb") as f:
        data = f.read().decode("unicode-escape")
        counts = Counter(data)
        for key, item in counts.items():
            if key not in set(string.printable):
                count += item
    return count


def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    the function finds the most common non-ascii characters for a document
    """
    count = {}
    with open(file_path, "rb") as f:
        data = f.read().decode("unicode-escape")
        counts = Counter(data)
        for key, item in counts.items():
            if key not in set(string.printable):
                count[key] = item
    res = "".join(sorted(count, key=lambda key: count[key], reverse=True)[:4])
    return res
