from collections import deque

q = deque()     # 큐 생성
answer = []     # 답을 넣을 배열

n, k = map(int, input().split())

for i in range(1, n+1):
    q.append(i)         # 큐에 1에서 n까지의 수 저장

while q:                
    for i in range(k-1):        # k-2 번째 인덱스까지만 꺼내서 다시 뒤에 넣기
        q.append(q.popleft())
    answer.append(q.popleft())  # k-1 번째 인덱스의 값은 꺼내와서 answer에 넣기

print('<', end='')
for j in range(len(answer)-1):
    print(f'{answer[j]},', end=' ')
print(answer[-1], end='')
print('>')