# すなわちどのように移動しても踏むことのない段はいくつあるか数えるプログラムを作成してください。

def fn(n, a, b):
    steps = [True] + [False] * n
    count = 0
    for i in range(n):
        if steps[i]:
            next_a = i + a
            if next_a < n:
                steps[next_a] = True
                next_b = i + b
                if next_b < n:
                    steps[next_b] = True
        else:
            count += 1
    return count

print(fn(10, 3, 8))

print(fn(10000, 6, 14))
