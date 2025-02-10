def subone():
    # 超时：时间复杂度o(n**2)
    n = input()
    s = input()
    nums = [int(x) for x in s.split()]
    n = len(nums)
    max_count = 0
    for i in range(n - 1):
        count = 1
        tmp = nums[i]
        for j in range(i, n):
            if nums[j] - tmp == 1:
                count += 1
                tmp = nums[j]
        max_count = max(max_count, count)
        if max_count >= n-i:
            break
    total = n - max_count
    print(total)

# 超时：时间复杂度o(n**2)
def dp(nums):
    n = len(nums)
    dp = [1]*n
    for i in range(n):
        for j in range(i):
            if nums[i]-1 == nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return n-max(dp)


def fn(nums):
    n = len(nums)
    max_count = 0
    for i in range(n-1):
        count = 1
        tmp = nums[i]
        for j in range(i+1, n):
            if nums[j] -tmp == 1:
                count += 1
                tmp = nums[j]
        max_count = max(max_count, count)
        if max_count >= n-i:
            break
    print("最大步进1递增子序列的长度为 %s" % max_count)
    # 移动次数为 n-k
    total = n -max_count
    return total

def lengthOfLIS(nums):
    tails, res = [0] * len(nums), 0
    for num in nums:
        i = 0
        j = res
        while i < j:
            m = (i + j) // 2
            if tails[m] < num:
                i = m + 1  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
            else:
                j = m
        tails[i] = num
        if j == res:
            res += 1
    return res

def length(nums):
    d = [nums[0]]
    count = 0
    for n in nums:
        # print(d)
        if n == d[-1]+1:
            d.append(n)
        if n > d[-1]+1:
            continue
        else:
            l, r = 0, len(d) - 1
            loc = r
            while l <= r:
                mid = (l + r) // 2
                if d[mid] >= n:
                    loc = mid
                    r = mid - 1
                else:
                    l = mid + 1

            d[loc] = n
    return len(d)


# [2, 3, 4, 1, 6, 7, 5]
# 排序找排序后原来元素的顺位和位置


# 时间复杂度：o(nlogn+n)= o(nlogn)
def dict_sort(nums):
    n = len(nums)
    # 对原数组先排序
    sort_nums = sorted(nums)

    # val:元素的位置，key:排序后元素的值
    d2 = {k: v for v, k in enumerate(sort_nums)}
    print(d2)

    # 找到原来元素的值所对应的顺位
    new_num = [d2[nums[i]] for i in range(n)]
    print(new_num)

    # val:顺位的位置。顺序的下标  key:原来元素的顺位
    d = {k: v for v, k in enumerate(new_num)}

    print(d)
    res = 1
    cnt = 1
    # i 元素的顺位：从1到l-1
    for i in range(n - 1):
        # d[i]:顺位的下标
        # 顺位的下标就是位于元素的位置
        if d[i] > d[i + 1]:
            res = max(res, cnt)
            cnt = 1
        else:
            cnt += 1
    return n - max(res, cnt)


# 优化：计数排序 时间复杂度o(n)
def count_sort_dict(nums):
    n = len(nums)
    # 对原数组先排序
    import copy
    before_sort_nums = copy.deepcopy(nums)
    max_num = max(nums)
    count = [0 for _ in range(max_num+1)]
    for val in nums:
        count[val] += 1
    nums.clear()
    for index, val in enumerate(count):
        for i in range(val):
            nums.append(index)

    print(before_sort_nums)
    print(nums)

    # val:元素的位置，key:排序后元素的值
    d2 = {k: v for v, k in enumerate(nums)}
    # 找到原来元素的值所对应的顺位
    new_num =[d2[before_sort_nums[i]] for i in range(n)]
    # val:顺位的位置。顺序的下标  key:原来元素的顺位
    d = {k: v for v, k in enumerate(new_num)}
    res = 1
    cnt = 1
    # i 元素的顺位：从1到l-1
    for i in range(n-1):
        # d[i]:顺位的下标
        # 顺位的下标就是位于元素的位置
        if d[i] > d[i+1] :
            res = max(res, cnt)
            cnt = 1
        else:
            cnt += 1
    return n - max(res, cnt)


nums1= [2, 3, 4, 1, 6, 7, 5]

print("answer is ",dp(nums1))



print("dict_sort is ", dict_sort(nums1))
print("count_sort_dict is ", count_sort_dict(nums1))




nums2= [2, 3, 1, 6, 4, 5]
# print(fn(nums2))
print("answer is ", dp(nums2))

print("dict_sort is ", dict_sort(nums2))

print("count_sort_dict is ", count_sort_dict(nums2))


nums3= [6, 5, 4, 3, 2, 1]

print("answer is ", dp(nums3))

print("dict_sort is ", dict_sort(nums3))

print("count_sort_dict is ", count_sort_dict(nums3))

nums4= [1, 2, 3, 4]
print("answer is ", dp(nums4))
print("count_sort_dict is ", count_sort_dict(nums4))
print("dict_sort is ", dict_sort(nums4))

