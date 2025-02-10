def quick_sort(L, left, right):
    if left >= right:
        return
    p = L[left]
    low = left
    high = right
    while low != high:
        while low < high and L[high] >= p: # 直到找到比p小的元素
            high -= 1
        L[low] = L[high]   # 将high指向的元素放到low的位置上(比基准P小的位置)
        while low < high and L[low] <= p:
            low += 1
        L[high] = L[low]

    L[low] = p # 放到中间的位置
    quick_sort(L, left, low-1)
    quick_sort(L, low+1, right)
    return L

a = [1, 15, 12, 3, 56, 42, 1, 44, 32, 25, 6, 7, 32]
# print(quick_sort(a, 0, len(a)-1))
quick_sort(a, 0, len(a)-1)
print(a)