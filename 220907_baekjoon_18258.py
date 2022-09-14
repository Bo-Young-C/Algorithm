from collections import deque
from sys import stdin

n = int(stdin.readline())

q = deque([])

# 큐를 이용해 풀기
for _ in range(n):
    lst = stdin.readline().split()
    if lst[0] == 'push':                # push 가 나오면 큐에 저장
            q.append(lst[1])
    elif lst[0] == 'pop':               # pop 이 나오면 큐에 원소 있을 때, 제거
        if len(q):                      # 원소 없으면 -1 출력
            print(q.popleft())
        else:
            print(-1)
    elif lst[0] == 'size':              # size 가 나오면 큐의 길이 출력
        print(len(q))
    elif lst[0] == 'empty':             # empty 가 나오면
        if len(q):                      # 큐에 원소 있을 시 0 을 출력
            print(0)
        else:                           # 없을 시 1을 출력
            print(1)
    elif lst[0] == 'front':             # front 가 나오면
        if len(q):                      # 큐에 원소 있을 시 맨 앞 원소 출력
            print(q[0])
        else:                           # 없을 시 -1 출력
            print(-1)
    elif lst[0] == 'back':              # back 이 나오면
        if len(q):                      # 큐에 원소 있을 시 맨 뒤 원소 출력
            print(q[-1])
        else:                           # 없을 시 -1 출력
            print(-1)