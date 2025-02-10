def fn28(L):
    a = list(set(L))
    if len(a) == len(L):
        print("NO")
    else:
        print("YES")

fn28([123, 432, 23])
fn28([123, 432, 23, 23, 23])