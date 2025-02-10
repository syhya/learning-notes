#
def fn1(a):
    a=list(a)
    a.reverse()
    #a = str(a)
    a = "".join(a) #list转str正确方法
    print(a)
fn1("xydz")

#拼接法
def fn2(a):
    b=""
    for i in range(len(a)):
        b=b+a[len(a)-i-1]
    print(b)
fn2("xydz")

#切片法
def fn3(a):
   print(a[::-1])
fn3("xydz")


