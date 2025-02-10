# 通用写法，不管复或者不重复
def fn(nums):
    # 一定要排序,重要
    nums.sort()
    result = []
    n = len(nums)
    visited = [0]*n

    def dfs(choices, path):
        if len(path) == n:
            result.append(list(path))
            return

        for i in range(n):
            # 剪枝1：当被访问过时visited[i] == 1 ,则跳过改元素.
            if visited[i] == 1:
                continue
            # 剪枝2：当前元素和前一个元素值相同（此处隐含这个元素的index>0），并且前一个元素还没有被使用过。
            # 如果不加visited[i-1] == 0,就会导致回溯中途过程中中断。
            elif i > 0 and choices[i] == choices[i-1] and visited[i-1] == 0:
                continue

            path.append(choices[i])
            visited[i] = 1
            dfs(choices, path)
            path.pop()
            # 回退后，重置为0.
            visited[i] = 0
    dfs(nums, [])
    return result


print(fn([1, 1, 2]))  # [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
print(fn([1, 2, 3]))  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(fn([3, 3, 0, 3]))



# 和前一个元素值相同（此处隐含这个元素的index>0），并且前一个元素还没有被使用过

# def permuteUnique(nums):
#     nums.sort()
#     res=[]
#     def backtrace(temp,nums):
#         if not nums:
#             res.append(temp)
#         for i in range(len(nums)):
#             # 剪枝条件：当前元素和元列表中前一个元素值相同
#
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             # 这种拼接方法是天然的标记，判断前一字符是否在循环里。
#             # nums[:i]+nums[i+1:]: 去除当前已经使用的元素
#             # temp+[nums[i]]：temp中加入当前使用过的元素
#             # 切片传入
#             backtrace(temp+[nums[i]], nums[:i]+nums[i+1:])
#     backtrace([],nums)
#     return res
