import sys
input = sys.stdin.readline

N = int(input())
nums = [0] * 10001      # 1~10000 자연수가 들어갈 카운팅 배열

for _ in range(N):
    n = int(input())
    nums[n] += 1        # 카운트

for i in range(10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)    # 카운트 수 만큼 차례대로 출력