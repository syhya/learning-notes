def merge(nums, left, mid, right):
    i = left
    j = mid +1
    result = []
    while i <= mid and j <= right:
        if nums[i] < nums[j]:
            result.append(nums[i])
            i += 1
        else:
            result.append(nums[j])
            j += 1
    while i <= mid :
        result.append(nums[i])
        i += 1
    while j <= right:
        result.append(nums[j])
        j += 1
    nums[left: right+1] = result

def merge_sort(nums, left, right):
    if left < right:
        mid = (left+right)//2
        merge_sort(nums, left, mid)
        merge_sort(nums, mid+1, right)
        merge(nums, left, mid, right)
    return nums

import random
nums = [i for i in range(100)]
random.shuffle(nums)
print(nums)
print(merge_sort(nums, 0, len(nums)-1))

