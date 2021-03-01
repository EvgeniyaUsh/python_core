from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    l = 0
    subarray_sum = 0

    while (len(nums) - k) >= l:
        count = 0
        mass = nums[l : k + l]
        for i in mass:
            count += i
        l += 1
        if count >= subarray_sum:
            subarray_sum = count

    return subarray_sum
