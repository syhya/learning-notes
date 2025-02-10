def fn1(a):
    b=""
    for i in range(len(a)):
        if i%2==0:
            b=b+a[i]
    print(b)
fn1("xyzwd")
fn1("xyzwd123456789")

#切片
def fn2(a):

    print(a[::2])
fn2("xyzwd")
fn2("xyzwd123456789")

#
def fn3(a):
    b = ""
    for i in range(0,len(a),2):
            b = b + a[i]
    print(b)


fn3("xyzwd")
fn3("xyzwd123456789")


