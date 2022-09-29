n, m = map(int, input().split())
a = min(n, m)                       # 두 수 중에 최소값 고르기
maxV = 0                            # 최대 공약수

for i in range(1, a+1):             # 1~최소값 으로 n, m을 나눠보기
    if n % i == 0 and m % i == 0:
        if maxV < i:                # 최대 공약수 갱신   
            maxV = i

print(maxV)
print(n*m//maxV)                    # 최소 공배수는 두 수의 곱을 최대 공약수로 나눈 것