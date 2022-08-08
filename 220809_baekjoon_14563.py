T = int(input()) # 주어진 자연수 개수
N = list(map(int, input().split())) # 배열만들기


for i in N: # 자연수 하나씩 꺼내어 반복
    n_sum = 0 # 각 자연수의 약수의 합을 저장할 변수
    # 약수 합
    for j in range(1, i):
        if i % j == 0:
           n_sum += j
    # 약수의 합 = 자연수 -> 완전수
    if n_sum == i :
        print('Perfect')
    # 약수의 합 > 자연수 -> 과잉수
    elif n_sum > i :
        print('Abundant')
    # 약수의 합 < 자연수 -> 부족수
    else:
        print('Deficient')