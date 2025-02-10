def factorial(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    return a

print(factorial(1))
print(factorial(2))
print(factorial(3))


print(factorial(9))