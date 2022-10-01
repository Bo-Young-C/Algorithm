# 지나야 하는 최소 칸 수를 구하기위해
# bfs(너비우선탐색) 사용!
# i : 현재 행, j : 현재 열
def bfs(i, j):
    visited = [[0]*M for _ in range(N)]
    q = [(0, 0)]       # 시작 위치 큐에 넣고 시작
    visited[0][0] = 1   # 시작 위치 방문 표시
    while q:
        i, j = q.pop(0)
        # 도착했다면 방문한 
        if i == N-1 and j == M-1:
            return visited[N-1][M-1]
        # 갈 수 있는 곳 탐색
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if maze[ni][nj] == '1' and visited[ni][nj] == 0:
                    # 방문표시
                    visited[ni][nj] = visited[i][j] + 1
                    # 다음 위치 큐에 추가하고 다음 위치로 이동해보자
                    q.append((ni, nj))
                

N, M = map(int, input().split())    # N : 세로 크기, M : 가로 크기
maze = [list(input()) for _ in range(N)]    # 미로정보

print(bfs(0, 0))


# ---------------------------------------
# 인덱스를 이용한 큐
def bfs(i, j):
    visited = [[0]*M for _ in range(N)]
    q = [(0, 0)]       # 시작 위치 큐에 넣고 시작
    front = -1
    rear = 0
    visited[0][0] = 1 
    while front != rear:
        front += 1
        i, j = q[front]
        if i == N-1 and j == M-1:
            return visited[N-1][M-1]
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if maze[ni][nj] == '1' and visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))
                    rear += 1
                

N, M = map(int, input().split())    
maze = [list(input()) for _ in range(N)]    

print(bfs(0, 0))


# -------------------------
# for 문 대신 if 문으로 구현한 코드
def bfs(i, j):
    visited = [[0]*M for _ in range(N)]
    q = [(0, 0)]       
    visited[0][0] = 1
    while q:
        i, j = q.pop(0)
        if i == N-1 and j == M-1:
            return visited[N-1][M-1]
        # 갈 수 있는 곳 탐색
        if i+1 < N and visited[i+1][j] == 0 and maze[i+1][j] == '1':
            visited[i+1][j] = visited[i][j] + 1
            q.append((i+1, j))
        if 0 <= i-1  and visited[i-1][j] == 0 and maze[i-1][j] == '1':
            visited[i-1][j] = visited[i][j] + 1
            q.append((i-1, j))
        if j + 1 < M and visited[i][j+1] == 0 and maze[i][j+1] == '1':
            visited[i][j+1] = visited[i][j] + 1
            q.append((i, j+1))
        if 0 <= j-1 and visited[i][j-1] == 0 and maze[i][j-1] == '1':
            visited[i][j-1] = visited[i][j] + 1
            q.append((i, j-1))
                

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)] 

print(bfs(0, 0))
