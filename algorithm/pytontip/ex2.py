#方法一

def fn1(L):
    L.sort()  #只是进行了排序无返回值
    print(L)
fn1([1,3,7,2])

#
def fn2(L):
    L1=[]
    for i in range(len(L)):
        L1.append(min(L))
        L.remove(min(L))
    print(L1)
fn2([1,3,7,2])

#冒泡排序
# 比较相邻的两个元素。如果第一个比第二个大则交换他们的位置(升序排列，降序则反过来)。
def fn3(L): #时间复杂度n**2
    for i in range(1,len(L)):  #循环次数很重要 外层n-1
        for j in range(0,len(L)-i): #内层从：n-1到1次
            if L[j]>L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
    print(L)

fn3([1,3,7,2])
fn3([10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21])
