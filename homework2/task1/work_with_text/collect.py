import re
from typing import List
from collections import Counter, OrderedDict
import string


def get_longest_diverse_words(file_path: str) -> List[str]:
    mass = []
    with open(file_path, 'rb') as f:
        data = f.read().decode('unicode-escape')
        data1 = re.findall(r"[\w']+|[.,!?;]", data)
        c = set(data1)

        for i in data1:
            mass.append(''.join(set(i)))
            # sorted(mass, key=lambda w: len(w),
            #         reverse=True)[:10]
        print(mass)


def get_rarest_char(file_path: str) -> str:
    with open(file_path, 'rb') as f:
        data = f.read().decode('unicode-escape')
        counts = Counter(data).most_common()
        return counts[-1][0]


def count_punctuation_chars(file_path: str) -> int:
    count = 0
    with open(file_path, 'rb') as f:
        data = f.read().decode('unicode-escape')
        counts = Counter(data)
        for key, item in counts.items():
            if key in set(string.punctuation):
                count += item
    return count


def count_non_ascii_chars(file_path: str) -> int:
    count = 0
    with open(file_path, 'rb') as f:
        data = f.read().decode('unicode-escape')
        counts = Counter(data)
        for key, item in counts.items():
            if key not in set(string.printable):
                count += item
    return count


def get_most_common_non_ascii_char(file_path: str) -> str:
    count = {}
    length = 0
    with open(file_path, 'rb') as f:
        data = f.read().decode('unicode-escape')
        counts = Counter(data)
        for key, item in counts.items():
            if key not in set(string.printable):
                count[key] = item
                if item > length:
                    length=item
    p = len(str(length))
    print(len(str(length)))
    return sorted(count, key=lambda key: count[key],
                  reverse=True)


file = 'data.txt'

print(get_most_common_non_ascii_char(file))
