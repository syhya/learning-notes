#动态规划来构造斐波那契数列
def fn43(n):
    f1, f2 = 1, 1
    f3 = 0
    if n <= 2:
        print(1 % 20132013)
    else:
        #（2，n) or (3,n+1)
        for i in range(2, n):
            f3 = f1+f2
            f1 = f2
            f2 = f3
        print(f3 % 20132013)

fn43(2)
fn43(210)