n1, n2 = map(int, input().split())
# car
nums1 = []
# people
nums2 = []

for i in range(n1):
    nums1.append(int(input()))
for j in range(n2):
    nums2.append(int(input()))
total = sum(nums2)
dp = [0] * n1

i = 0
j = 0
while sum(dp) != total:
    if nums2[i] > nums1[j]:
        dp[j] += nums1[j]
        tmp = nums2[i] - nums1[j]
        nums2[i] = tmp
        j += 1
        if j == n1:
            j = 0
    elif nums2[i] <= nums1[j]:
        dp[j] += nums2[i]
        i += 1
        j += 1
        if j == n1:
            j = 0
for i in dp:
    print(i)
