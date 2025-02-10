def delete_element(nums):
    j = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[j]:
            continue
        else:
            nums[j+1] = nums[i]
            j += 1
    print(j)
    return nums


print(delete_element([1, 1, 2]))
print(delete_element([0, 0, 1, 1, 2, 2, 3, 3, 4]))
