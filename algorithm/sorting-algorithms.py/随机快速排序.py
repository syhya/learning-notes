import random
# 基准"元素随机产生
def partition(nums, left, right):
    # 生成[left,right]之间的一个随机的索引
    random_index = random.randint(left, right)
    # 重点:把随机到的元素和left所指向的元素交换
    nums[left], nums[random_index] = nums[random_index],nums[left]
    p = nums[left]   # 这样基准相当于随机取的元素

    while left < right:
        while left < right and nums[right] >= p:  # 从右边找比p小的数
            right -= 1  # 往左走一位
        nums[left] = nums[right]  # 把右边的值放到左边空位上
        while left < right and nums[left] <= p:
            left += 1
        nums[right] = nums[left]  # 把左边的值放到右边空位上
    nums[left] = p  # 把p归位到left和right相遇的位置
    return left

def quick_sort(nums, left, right):
    if left < right:  # 这个是递归的条件。当不满足这个条件时。终止递归
        mid = partition(nums, left, right) # 因为要递归，所以放入的是left和right
        quick_sort(nums, left, mid - 1)
        quick_sort(nums, mid+1, right)

    '''   
    elif left >= right:   # 递归终止条件，可以不写。
        return 
    '''

nums = [3,3,3,3,3,3,3,3,3]
quick_sort(nums, 0, len(nums)-1)
print(nums[-1])


