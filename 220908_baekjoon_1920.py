def binary(target):             # 이진 탐색
    start = 0
    end = n - 1
    while start <= end:
        middle = (start + end) // 2
        if nums[middle] == target:
            return True
        elif target < nums[middle]:
            end = middle-1
        elif target > nums[middle]:
            start = middle + 1
    return False

n = int(input())

nums = list(map(int, input().split()))
m = int(input())
nums.sort()     # 정렬


lst = list(map(int, input().split()))

# 하나씩 존재하는지 검사
for i in range(m):
    if binary(lst[i]):      # 찾으면 1 출력
        print(1)    
    else:                   # 찾지못하면 0 출력
        print(0)