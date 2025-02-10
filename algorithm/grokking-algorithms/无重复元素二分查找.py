# 二分查找,排好序了的
def fn1(L, a):
    low = 0
    high = len(L)-1
    while low <= high:    # 条件：只要范围没缩小到只有一个元素
        mid = int((low + high) / 2)  # 强制转换向下取整,mid在循环体内变化。
        if a == L[mid]:
            return mid
        elif a > L[mid]:
            low = mid+1
        else:
            high = mid-1
    return None 

print(fn1([1,2,3,4],3))
print(fn1([1,2,3,4],10))