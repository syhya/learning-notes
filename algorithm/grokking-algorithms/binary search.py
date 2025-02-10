# 找到大于等于val的第一个元素的index
def search(nums, val):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] < val:
            left = mid+1
        else:  # 等号在这里表示，find最左边值为val元素的index
            right = mid-1

    return left

nums1 = [1,2,3,4,4,4,7,7,7,10]
print("len is %s" % len(nums1))
print(search(nums1, 4))
a = search(nums1, 5)-1
print(a)