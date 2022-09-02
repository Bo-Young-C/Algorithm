l = int(input())                            # 집합 S의 크기
nums = list(map(int, input().split()))      # 집합에 포함된 정수들
n = int(input())
# n 을 포함하는 좋은 구간의 개수
# A와 B는 양의 정수, A < B 를 만족
# A <= x <= B 를 만족하는 모든 정수 x 가 집합 S에 속하지 않는다.
# n 을 포함하는 좋은 구간의 개수

# 0부터 가능하니까 추가
nums.append(0)
# 집합 S 정렬
nums.sort()

ans = 0     
for i in range(l):                      # nums 순회
    if nums[i] == n or nums[i+1] == n:  # 만약 nums 의 원소가 n 과 같다면 좋은 구간 개수 없음, 반복종료
        ans = 0
        break
    elif nums[i] < n < nums[i+1]:       # 원소 사이에 있다면 (n-왼쪽 원소)*(오른쪽-원소)-1 개만큼 좋은 구간 존재
        ans = (n-nums[i])*(nums[i+1]-n)-1
        break
print(ans)
