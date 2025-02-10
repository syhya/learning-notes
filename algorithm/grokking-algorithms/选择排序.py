#选择排序 升序
def fn2(L):
    for i in range(len(L)-1):  # 最后只剩2个数，把小的换到前面就行了。
        min_index = i  # 将起始元素设为最小元素
        for j in range(i+1,len(L)):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]

    return L

print(fn2([1,15,12,3,56,42,1,44,32,25,6,7,32]))


#参考写法：
def selection_sort(arr):
    """选择排序"""
    # 第一层for表示循环选择的遍数
    for i in range(len(arr) - 1):
        # 将起始元素设为最小元素
        min_index = i
        # 第二层for表示最小元素和后面的元素逐个比较
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                # 如果当前元素比最小元素小，则把当前元素角标记为最小元素角标
                min_index = j
        # 查找一遍后将最小元素与起始元素互换
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

print(selection_sort([1,15,12,3,56,42,1,44,32,25,6,7,32]))