def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums)//2
    left, right = nums[:mid], nums[mid:]
    return merge(merge_sort(left), merge_sort(right))


import random
nums = [i for i in range(1000)]
random.shuffle(nums)
print(nums)
print()
print(merge_sort(nums))
