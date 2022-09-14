import sys
# 런타임에러가 떠서 반복제한을 늘려주기!!
sys.setrecursionlimit(10**9)

# dfs
def dfs(node):
    visited[node] = True
    for i in arr[node]:
        if not visited[i]:
            ans[i] = node
            dfs(i)
    return

# n : 노드의 개수, arr : 연결 정보
# visited : 방문체크, ans : 노드의 부모 저장된 배열
n = int(sys.stdin.readline())
arr = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
ans = [1 for _ in range(n+1)]

for i in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

dfs(1)      # dfs 돌리기

for i in range(2, len(ans)):
    print(ans[i])