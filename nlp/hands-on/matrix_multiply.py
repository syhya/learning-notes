import torch.nn as nn
import torch
# arrary
# a: (m, n) * b: (n, p) -> c: (m, p) 
def matrix_multiply(a, b):
    m = len(a)
    n = len(a[0])
    p = len(b[0])
    c = [[0] * p for _ in range(m)]
    

    # matrix multiply
    # line m, row: p
    for i in range(m):
        for j in range(p):
            # 计算C[i][j]，即A的第i行和B的第j列的点积
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c

# a: (m, n) * b: (n, p) -> c: (m, p) 
def matrix_multiply_torch(a, b):
    m, n = a.shape
    _, p = b.shape
    c = torch.zeros((m, p))
    for i in range(m):
        for j in range(p):
            # boardcast: A[0, :] * B[:, 0] == [a11 * b11, a12 * b21, a13 * b31]
            c[i][j] = torch.sum(a[i, :] * b[:, j])
    return c



# test data
# a (3, 2)
a = [[1, 2],
     [1, 3],
     [1, 4]]
# b (2, 3)
b = [[1, 1, 1],
     [2, 2, 2]]
tensor_a = torch.tensor(a)
tensor_b = torch.tensor(b)
torch_c = torch.matmul(tensor_a, tensor_b)

torch_c_from_zero = matrix_multiply_torch(tensor_a, tensor_b)
print(torch_c_from_zero)
print(torch_c)
c = matrix_multiply(a, b)
print(c)