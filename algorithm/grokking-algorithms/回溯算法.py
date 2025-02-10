#41.全排列


def fn(nums):
    length = len(nums)          #这里len([1,2,3])为3
    res = []

    def dfs(numset, checked, deepth):
        if deepth == length:
            res.append(checked[:])

        for i in range(length):
            if numset[i] not in checked:
                checked.append(nums[i])   # 先向下递归
                dfs(numset, checked, deepth+1)         # 内部递归
                checked.pop()   # 回溯到上一个节点
    dfs(nums, [], 0)
    return res


# 重要的写法:用choices而不是nums避免混淆。
def fn2(nums):
    result = []
    def trace(path, choices):  # 回溯函数，这里用choices而不是nums避免混淆。
        if len(path) == len(nums):  # 结束条件
            result.append(list(path))  # 结果添加
            return
        for val in choices:  # 可选选则
            if val in path:  # 剪枝操作,用过的元素不能再用。
                continue

            path.append(val)   # 路径添加
            trace(path, choices)  # 下一节点， 递归
            path.pop()  # 路径回溯

    trace([], nums)
    return result

# 通 用重要写法
def fn3(nums):
    n = len(nums)
    result = []
    visited = n * [0]

    def trace(choices, path):
        if len(path) == n:
            result.append(list(path))
            return
        for i in range(n):
            if visited[i] == 1:
                continue
            path.append(choices[i])
            visited[i] = 1
            trace(choices, path)
            path.pop()
            visited[i] = 0
    trace(nums, [])
    return result


print(fn([1,2,3]))
print(fn2([1,2,3]))
print(fn3([1,2,3]))