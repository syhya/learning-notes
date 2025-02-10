# 浅拷贝，深拷贝
a = [[0] * 2] * 6
b = [[0] * 2 for _ in range(6)]

print(len(a))
print(len(b))
a[0][0] = 1
print(a)
b[0][0] = 1
print(b)