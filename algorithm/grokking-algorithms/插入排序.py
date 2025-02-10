# 插入排序： 不是交换。
def fn(L):
    for i in range(1, len(L)):
        a = L[i]
        j = i
        while j>0 and a<L[j-1]:
            L[j] = L[j-1]  #将满足条件的数字往列表后面移动
            j -= 1
        L[j] = a
    return L
print(fn([1,15,12,3,56,42,1,44,32,25,6,7,32]))
