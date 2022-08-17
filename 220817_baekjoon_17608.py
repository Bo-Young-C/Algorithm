N = int(input())    # 막대기 개수
bars = [int(input()) for _ in range(N)]
# 스택으로 풀기
max_bar = bars[-1]  # 가장 오른쪽 막대기부터 비교
result = 1          # 가장 오른쪽 막대기는 항상 보이므로 1로 설정
for i in range(N):
    temp = bars.pop()   # temp 에 bars의 top 위치의 원소 꺼내옴
    if max_bar < temp:  # 크면 -> 카운트 해주고 max_bar를 temp로 바꿈
        result += 1
        max_bar = temp
print(result)