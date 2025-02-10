def outplace_quick(nums):
    if len(nums) < 2:
        return nums
    p = nums[0]
    left = [i for i in nums[1:] if i <= p]
    right = [j for j in nums[1:] if j >= p]
    return outplace_quick(left) + [p] + outplace_quick(right)

nums = [5,7,4,6,3,1,2,9,8]
print(outplace_quick(nums))

