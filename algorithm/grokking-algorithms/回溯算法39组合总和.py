# 限制下一次选择的起点，是基于本次的选择，这样下一次就不会选到本次选择同层左边的数
# 每一次搜索的时候设置 下一轮搜索的起点 start
def combination(candidates, target):
    res = []
    def dfs(start, candidates, target, path):
        if target == 0:
            res.append(list(path))
            return

        for i in range(start, len(candidates)):  # 枚举当前可选的数，从start开始
            if candidates[i] <= target:
                path.append(candidates[i])
                # print("每次结果为%s" % path)
                # 下次就不会选到i号位置左边的数
                # 注意，子递归传了 i 而不是 i+1 ，
                # 因为元素可以重复选入集合，如果传 i+1 就不重复了。
                dfs(i, candidates, target-candidates[i], path)
                path.pop()

    dfs(0, candidates, target, [])
    return res

print(combination([2,3,6,7], 7))

print(combination([2, 3, 5], 8))

print(combination([2], 1))
