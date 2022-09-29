N = int(input())

nums = [list(map(int, input().split())) for _ in range(N)]

nums.sort()         # 정렬

for i in nums:
    print(*i)