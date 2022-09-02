n = int(input())

nums = list(int(input()) for _ in range(n))

# 시간초과가 떠서 sorted 함수로 통과....
for i in sorted(nums):
    print(i)


# 버블정렬
# for i in range(n-1, 0, -1):
#     for j in range(i):
#         if nums[j] >= nums[j+1]:
#             nums[j], nums[j+1] = nums[j+1], nums[j]

# for i in nums:
#     print(i)