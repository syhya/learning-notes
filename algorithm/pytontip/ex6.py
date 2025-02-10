def f6():
    for i in range(2, 101):
        if i == 2:
            print(i, end=" ")
        elif i <= 7 and i % 2 != 0:
            print(i, end=" ")
        elif i % 2 and i % 3 and i % 5 and i % 7 != 0 and i != 97:
            print(i, end=" ")
        elif i == 97:
            return i
            break

print(f6())

