import random
def r_outplace_quick(nums, left, right):
    if len(nums) < 2:
        return nums
    random_index = random.randint(0, len(nums)-1)
    nums[0], nums[random_index] = nums[random_index], nums[0]

    p = nums[0]
    left = [i for i in nums[1:] if i <= p]  # 只能有一个等号
    right = [i for i in nums[1:] if i > p]
    return r_outplace_quick(left)+[p]+r_outplace_quick(right)

nums = [11,1,1,1,15,7,4,6,3,1,2,9,8]
print(r_outplace_quick(nums))