from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    length = len(a)
    count = 0
    for i in range(length):
        for j in range(length):
            for k in range(length):
                for n in range(length):
                    summ = a[i] + b[j] + c[k] + d[n]
                    if summ == 0:
                        count += 1
    return count
