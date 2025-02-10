import random

def outquicksort(nums):
    if len(nums) < 2:
        return nums
    p = nums[0]
    left = [i for i in nums[1:] if i <= p]
    right = [i for i in nums[1:] if i > p]
    return outquicksort(left)+[p]+outquicksort(right)

print(outquicksort([2,3,3,4,2,2,1,1]))


def inplace_quicksort(nums, left, right):
    p = nums[0]
    i = 1
    j = len(nums)-1
    while left < right:
        while nums[i] >= p and nums[j] <= p:



