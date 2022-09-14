N, M = map(int, input().split())            # MxN 크기의 체스판
board = [list(input()) for _ in range(N)]   # 체스판 정보
result = []                                 # 8x8 크기로 자른 체스판에서 고쳐야 할 색의 개수

for i in range(N-7):
    for j in range(M-7):
        cntw = 0                            # 시작이 흰 색인 경우
        cntb = 0                            # 시작이 검은 색인 경우
        for k in range(i, i+8):
            for h in range(j, j+8):
                if (k + h) % 2 == 0:        # 합이 짝수이면 같은 색을 가져야 함
                    if board[k][h] != 'W':  # 흰색이 아니라면 고쳐야 함
                        cntw += 1
                    if board[k][h] != 'B':  # 검은색이 아니라면 고쳐야 함
                        cntb += 1
                else:
                    if board[k][h] != 'B':  # 합이 홀수이면 시작과 다른 색을 가져야 함
                        cntw += 1           # 검은색이 아니라면 고쳐야 함
                    if board[k][h] != 'W':
                        cntb += 1           # 흰색이 아니라면 고쳐야 함
        result += [cntw]
        result += [cntb]
# 최소값 구하기
ans = result[0]
for i in result:
    if i < ans:
        ans = i 
print(ans)