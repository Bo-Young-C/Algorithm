T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    cnt = 0                     # 0의 개수
    for i in range(n, m+1):
        for j in str(i):        # 문자열로 바꿔서 하나씩 순회
            if j == '0':        # 0이면 카운트!
                cnt += 1
    print(cnt)