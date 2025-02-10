
def binary_search(nums, val):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right) // 2
        if val == nums[mid]:
            return mid
        elif val < nums[mid]:
            right = mid-1
        else:
            left = mid+1
    return None

print(binary_search([0, 1, 2,4,4,4,4,4,4 ,5, 6, 7], 4))



