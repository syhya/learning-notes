def fn(s1,s2):
    a = len(s1)
    b = len(s2)
    cell = [[0] * (b+1) for _ in range(a+1)]  # 这里的顺序很重要先b后a,利用 for 循环生成每一行，则每一行都是全新的.
    for i in range(1, a+1):   # 边界重点
        for j in range(1, b+1):
            if s1[i-1] == s2[j-1]:  # 两个字符串从0开始
                cell[i][j] = cell[i-1][j-1]+1
            else:
                cell[i][j] = max(cell[i-1][j], cell[i][j-1])

    return cell[len(s1)][len(s2)]

print(fn("FOSH","FORT")) #2
print(fn("FOSH","FISH")) #3
print(fn("abcde","ace")) #3
print(fn("oxcpqrsvwf","shmtulqrypy")) # 2







