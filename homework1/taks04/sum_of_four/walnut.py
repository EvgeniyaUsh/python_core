from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """
    the function counts the number of tuples (i, j, k, l)
    such that A [i] + B [j] + C [k] + D [l] is equal to zero.
    """
    length = len(a)
    count = 0
    dic = {}
    for i in range(length):
        for j in range(length):
            summ = a[i] + b[j]
            dic[summ] = dic.get(summ, 0) + 1
    for i in range(length):
        for j in range(length):
            count += dic.get(-c[i] - d[j], 0)
    return count
