import numpy as np


def fn(str_1,str_2):
        a = 0
        size = (len(str_1), len(str_2))   # 元组
        cell = np.zeros(size)   # 放入元组构造二维零矩阵
        for i in range(len(str_1)):
            for j in range(len(str_2)):
                if str_1[i] == str_2[j]:
                    cell[i][j] = cell[i-1][j-1]+1
                    if cell[i][j] > a:
                        a = cell[i][j]
                else:
                    cell[i][j] = 0

        return a



print(fn("HISH","FISH"))  # 3
print(fn("VISTA","HISH")) # 2

