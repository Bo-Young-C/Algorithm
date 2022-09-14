n, m = map(int, input().split())

lst = [list(map(int, input())) for _ in range(n)]
# n 과 m 중 최소값 찾기
if n > m:
    a = m
else:
    a = n
# 꼭짓점의 수가 같은 가장 큰 정사각형 찾기 
ans = 0     # 가장 큰 정사각형의 크기를 넣을 변수
for i in range(n):
    for j in range(m):
        for k in range(a):
            # 범위 안인지 확인
            if (i+k < n) and (j+k < m):
                # 꼭짓점 같은지 확인
                if lst[i][j] == lst[i][j + k] == lst[i+k][j] == lst[i+k][j+k]:
                    # 현재 ans 보다 크면 갱신
                    if ans < (k+1)**2:
                        ans = (k+1)**2

print(ans)