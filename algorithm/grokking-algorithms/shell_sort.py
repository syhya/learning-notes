def insert_sort_gap(nums, gap):
    for i in range(gap, len(nums)):
        tmp = nums[i]
        j = i-gap
        while j >= 0 and nums[j] > tmp:
            nums[j+gap] = nums[j]
            j -= gap
        nums[j+gap] = tmp


def shell_sort(nums):
    d = len(nums)// 2
    while d >= 1:
        insert_sort_gap(nums, d)
        d //= 2

import random
nums = [i for i in range(1000)]
random.shuffle(nums)
print(nums)
shell_sort(nums)
print(nums)

