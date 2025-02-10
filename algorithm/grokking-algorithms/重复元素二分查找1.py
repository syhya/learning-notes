def searchRange(nums, target):
    def binary_search(nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    if len(nums) == 0:
        return [-1, -1]
    findleft = binary_search(nums, target)
    findright = binary_search(nums, target + 1) - 1

    if nums[findright] == target and nums[findright] == target:
        return [findleft] + [findright]
    else:
        return [-1, -1]



