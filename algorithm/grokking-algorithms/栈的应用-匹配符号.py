def par(s):
    dic = {
        ")": "(",
        "]": "[",
        "}": "{"}
    stack = []
    for i in s:
        # 1.if 数组不为空：可以执行后面
        # 2.字典 in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。
        if stack and i in dic:
            if stack[-1] == dic[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)

    if  stack == []:
        return True
    else:
        return False


print(par("((((())"))
print(par("{{([])}}"))
print(par("(])"))







