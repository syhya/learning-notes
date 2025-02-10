# 简洁写法
def fn(L):
    if len(L) <2:
        return L
    else:
        p = L[0]      #p:pivot所选的基准值
        low = [i for i in L[1:] if i <= p]  # 这里的等于号必不可少,要除去所选的那个基准数字。
        high = [i for i in L[1:] if i > p]  # 重点：只能有一个等号
        return fn(low)+[p]+fn(high)   #注意需要重新将p放在数组中

print(fn(([1, 15, 12, 3, 56, 42, 1, 44, 32, 25, 6, 7, 32])))







