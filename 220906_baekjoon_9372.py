from collections import deque

# 시간초과로 인해 다른 방법으로 제출
T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())
    print(n - 1)

# bfs 로 풀기

def bfs(v):
    q = deque([v])
    visited[v] = 1
    cnt = 0
    while q:
        q.popleft()
        for i in range(1, n+1):
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                cnt += 1
    return cnt

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    graph = [[0]*(n+1) for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1

    visited = [0] * (n+1)
    print(bfs(1))