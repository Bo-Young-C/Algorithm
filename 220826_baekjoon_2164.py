from collections import deque   # 시간초과를 막기 위해 파이썬 안의 모듈 이용!

N = int(input())
cards = deque([ i for i in range(1, N+1)])      # deque로 만들기

while len(cards) > 1:           # 마지막 남은 원소가 목적이니까 길이가 1이면 반복 종료 설정
    cards.popleft()             # 맨 위 카드 버림
    tmp = cards.popleft()       # 그 다음 맨 위 카드는 마지막으로 다시 넣기
    cards.append(tmp)           

print(cards[0])