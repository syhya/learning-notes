# 冒泡升序

# 相当于依次在末尾放入最大的元素。
def b_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

import random
test_1 = [i for i in range(15)]
random.shuffle(test_1)
print(test_1)
print(b_sort(test_1))





#另外的写法。
# 这样相当于依次在首位放入最小的元素。
def fn(L):
    for i in range(len(L)-1):
        for j in range(i+1, len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
    return L

print(fn(([1,15,12,3,56,42,1,44,32,25,6,7,32])))


# 短冒泡升序,如果在第n次遍历中没有交换元素，停止继续遍历。

def fn2(L):
    exchanges = True
    p = len(L)-1
    while p > 0 and exchanges == True:
        exchanges = False
        for i in range(p):
            if L[i] > L[i+1]:
                exchanges = True
                L[i], L[i+1] = L[i+1], L[i]
        p -= 1
    return L

print(fn2(([1,15,12,3,56,42,1,44,32,25,6,7,32])))