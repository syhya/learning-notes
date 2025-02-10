def partition(nums, left, right):
    p = nums[left]
    while left < right:
        while left < right and nums[right] >= p:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= p:
            left += 1
        nums[right] = nums[left]
    nums[left] = p
    return left

def quick_sort(nums, left, right):
    if left >= right:
        return
    else:
        mid = partition(nums, left, right)
        quick_sort(nums, left, mid-1)
        quick_sort(nums, mid+1 ,right)
        return nums

nums = [5,7,4,6,3,1,2,9,8]
print(quick_sort(nums, 0, len(nums)-1))