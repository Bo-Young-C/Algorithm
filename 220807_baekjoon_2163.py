N, M = map(int, input().split()) # N, M : 초콜릿 가로, 세로 크기

# 최소 쪼개기 횟수
print(0 if N == M == 1 else N*M-1)