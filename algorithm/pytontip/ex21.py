def fn(a):
    print("YES" if a == a[::-1] else "NO")
fn("abcba")
fn("abcbaa")