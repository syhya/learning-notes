def abc_dp():
    k, s, t = [int(x) for x in input().split()]
    dp = [0] * 50
    dp[0] = "ABC"
    for i in range(1, k):
        dp[i] = "A" + dp[i - 1] + "B" + dp[i - 1] + "C"
    print(dp[k - 1][s - 1:t])


# 滚动数组
def abc_dp():
    k, s, t = [int(x) for x in input().split()]

    dp0 = "ABC"
    for i in range(1, k):
        dp1 = "A" + dp0 + "B" + dp0 + "C"
        dp0 = dp1
    print(dp1[s - 1:t])


# 直接字符串相加超时。
# https://www.cnblogs.com/chenjingyi/p/5741901.html
# 字符串几种拼接方式比较


# join拼接
def abc_dp():
    k, s, t = [int(x) for x in input().split()]

    dp0 = "ABC"
    for i in range(1, k):
        dp1 = "".join(["A", dp0, "B", dp0, "C"])
        dp0 = dp1
    print(dp1[s - 1:t])
#


#  字符串溢出
def abc_dp(k, s, t):
    # k, s, t = [int(x) for x in input().split()]

    dp0 = "ABC"
    for i in range(1, k):
        dp1 = "".join(["A", dp0, "B", dp0, "C"])
        dp0 = dp1

    print(dp1[s-1: t])
    # print(len(dp1))

# 全局变量的使用方法
# 递归
global c
c = ""
def abcop(k, s, t):
    def fn(n):
        if n == 0:
            return 0
        elif n >= 1:
            return 2*fn(n-1)+3
    def g(p, q):
        global c
        if p == 1:
            c += "A"
        elif (1<p and p < fn(q-1)+2):
            g(p-1, q-1)
        elif p == fn(q-1)+2:
            c += "B"

        elif fn(q-1)+2 < p and p < fn(q):
            g(p-fn(q-1)-2, q-1)
        elif p == fn(q):
            c += 'C'

    for i in range(s, t+1, 1):
       g(i, k)

    print(c)


abcop(50, 6, 4)
abc_dp(20, 6, 20)




# abc_dp(6)
# abc_dp(5)