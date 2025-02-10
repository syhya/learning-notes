import numpy as np

# 这种方法效率低
def fn(s1,s2):
    a = 0
    size = (len(s1)+1, len(s2)+1)   # 当 i = 0 或者 j = 0 时，dp[i][j] 初始化为 0.
    cell = np.zeros(size, dtype=int)   # 默认为float型
    for i in range(1, len(s1)+1):   # 边界重点
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:  # 两个字符串从0开始
                cell[i][j] = cell[i-1][j-1]+1
                if cell[i][j] > a:
                    a = cell[i][j]
            else:
                cell[i][j] = max(cell[i-1][j], cell[i][j-1])

    return int(a)

print(fn("FOSH","FORT")) #2
print(fn("FOSH","FISH")) #3
print(fn("abcde","ace")) #3

print(fn("oxcpqrsvwf","shmtulqrypy")) # 2



