def bucket_sort(nums, n = 100, max_num = 10000):
    buckets = [[] for _ in range(n)]  # 创建桶。用二维列表来存放桶
    for val in nums:
        i = min(val//(max_num//n), n-1)  # i 表示var放到几号桶里，防止最后一个元素越界。
        buckets[i].append(val) # 把var加到桶里面
        # 保持桶内的顺序
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    nums_sorted = []
    for buc in buckets:
        nums_sorted.extend(buc)  # extend加入列表
    return nums_sorted

import random
nums = [random.randint(0, 10000) for i in range(100000)]
a = bucket_sort(nums)
print(a)