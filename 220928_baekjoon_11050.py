N, K = map(int, input().split())
a = N          # nPk 값을 저장할 변수
b = K          # k! 값을 저장할 변수
if K == 0:     # k 가 0이면 nC0 = 1
    print(1)
else:
    # nPk, k! 구하기
    for i in range(1, K):
        a *= N-i
        b *= K-i
    print(a//b)