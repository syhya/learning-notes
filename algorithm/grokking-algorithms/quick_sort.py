def quick_sort(nums):
    if len(nums) < 2:
        return nums
    p = nums[0]
    left = [i for i in nums[1:] if i <= p]
    right = [i for i in nums[1:] if i > p]
    return quick_sort(left)+[p]+quick_sort(right)

print(quick_sort([3,2,1,5,6,4]))