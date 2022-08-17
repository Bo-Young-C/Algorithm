N, M = map(int, input().split())    # 배열 크기(행, 열)
arr = [list(map(int, input().split())) for _ in range(N)]   # 배열
K = int(input())    # 합을 구할 부분 개수
a = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        a[i][j] = arr[i-1][j-1] + a[i][j-1] + a[i-1][j] - a[i-1][j-1]

for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(a[x][y] - a[x][j-1] - a[i-1][y] + a[i-1][j-1])

