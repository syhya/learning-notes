import random

def radix_sort(nums):
    max_num = max(nums)
    k = 0
    while 10**k <= max_num:
        buckets = [[] for _ in range(10)]
        for i in nums:
            # 978 k=1   987//10->98  98%10->8  k=2  987//100->9 9%10=>9
            digit = (i//10**k) % 10
            # 完成分桶
            buckets[digit].append(i)
        nums.clear()
        # 把数重写回nums
        for j in buckets:
            nums.extend(j)
        k += 1


# nums = list(range(10000))
# random.shuffle(nums)
# print(nums)
# radix_sort(nums)
# print(nums)

nums = [1,3,100]
radix_sort(nums)
print(nums)


