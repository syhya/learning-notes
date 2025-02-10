import stack_module

def par(a):  # a为要匹配的东西
    s = stack_module.Stack()
    i = 0
    # 利用栈如果遇到左括号就push,右括号就pop.
    while i <len(a):
        symbol = a[i]
        if  s.isEmpty() and symbol == ")":
            return False
        elif symbol == "(":
            s.push(symbol)
        else:
            s.pop()
        i += 1

    if s.isEmpty() and i == len(a):
        return True
    else:
        return False

print(par("(()()()())"))
print(par("(((())))"))
print(par("(()((())()))"))


print(par("()))"))
print(par("((((())"))
print(par("(()()(()"))


