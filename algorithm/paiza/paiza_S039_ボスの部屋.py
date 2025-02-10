# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

def fn1():
    m, n = [int(x) for x in input().split()]
    matrix = [[0] * n for _ in range(m)]
    # print(dp)
    for i in range(m):
        s = input()
        for j in range(len(s)):
            if s[j] == "#":
                matrix[i][j] = "0"
            else:
                matrix[i][j] = "1"

    print(matrix)

    if not matrix or not matrix[0]:
        print(0)
    row = len(matrix)
    col = len(matrix[0])
    height = [0] * (col + 2)
    res = 0
    for i in range(row):
        stack = []
        for j in range(col + 2):
            if 1 <= j <= col:
                if matrix[i][j - 1] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            while stack and height[stack[-1]] > height[j]:
                cur = stack.pop()
                res = max(res, (j - stack[-1] - 1) * height[cur])
            stack.append(j)
    print(res)



def fn2():
    m, n = [int(x) for x in input().split()]
    matrix = [[0] * n for _ in range(m)]
    # print(dp)
    for i in range(m):
        s = input()
        for j in range(len(s)):
            if s[j] == "#":
                matrix[i][j] = "0"
            else:
                matrix[i][j] = "1"

    print(matrix)
    if not matrix or not matrix[0]:
                return 0
    row = len(matrix)
    col = len(matrix[0])
    height = [0] * (col+1)
    res = 0
    for i in range(row):
        for j in range(col):
            # 前缀和
            # 记录当前位置上方连续“1”的个数
            if matrix[i][j] == "1":
                height[j] += 1
            else:
                height[j] = 0
            # print(height)

        # 单调栈
        # height :84题的矩形的高度
        stack = [-1]
        for k, val in enumerate(height):
            while stack and height[stack[-1]] > val:
                index = stack.pop()
                res = max(res, height[index]*(k-stack[-1]-1))
                # print(res)
            stack.append(k)
    return res