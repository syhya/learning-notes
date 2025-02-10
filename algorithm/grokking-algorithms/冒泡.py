def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

# 改进冒泡
#如果冒泡排序中的一趟排序没有发生交换，则说明列表已经有序，可以直接结束算法。
def bubble_sort_r(nums):
    for i in range(len(nums)-1):
        exchange = False
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                exchange = True
        if not exchange:
            return nums
    return nums

li = [i for i in range(25)]
import random
random.shuffle(li)
print(li)
print(bubble_sort(li))
print(bubble_sort_r(li))

