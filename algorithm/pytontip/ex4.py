def fn1(a):
    print(','.join(sorted(str(i) for i in a)))
#内建函数 sorted方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

fn1({"tow":55,4:2,3:3,"four":1,1:2,3:3})
fn1({1:55,4:2,3:3,3:1,1:2,3:3})

for i in {1:55,4:2,3:3,3:1,1:2,3:3}:
    print(i)  #只打键的值，相同的值不重复打印。


def fn2(a):
    print(','.join(sorted(map(str, a.keys())))) #利用map映射转换为字符串
#list 的 sort方法返回的是对已经存在的列表进行操作
#内建函数 sorted方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
fn2({"tow":55,4:2,3:3,"four":1,1:2,3:3})
fn2({1:55,4:2,3:3,3:1,1:2,3:3})




