def bubble_sort(nums):
    for i in range(len(nums)-1):
        flag = False
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = True
        if not flag:
            return nums
    return nums


nums = [5,7,4,6,3,1,2,9,8]
print(bubble_sort(nums))