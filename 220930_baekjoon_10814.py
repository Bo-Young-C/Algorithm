N = int(input())

members = [list(input().split()) for _ in range(N)]
members.sort(key=lambda x:int(x[0]))        # sort의 key=lambda를 이용해서 나이순으로 정렬
# key=lambda 를 쓰지 않고 그냥 sort를 사용하면, 나이순과 이름의 사전순 둘다 적용됨
for i in range(N):
    print(*members[i])
