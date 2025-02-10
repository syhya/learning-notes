# 要知道所排序列表的范围
def count_sort(nums, max_count):
    count = [0 for _ in range(max_count+1)]
    for val in nums:
        count[val] += 1
    nums.clear()
    for index, val in enumerate(count):
        for i in range(val):
            nums.append(index)

nums = [3,0,0,0,0,2,1,4,141,12,24,124,124,1,24,12,4,1]
count_sort(nums, 141)
print(nums)