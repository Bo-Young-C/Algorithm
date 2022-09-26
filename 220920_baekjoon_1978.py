import math

# 소수 판별
def primenumber(x):
    # 2~x의 제곱근으로 나누어 떨어지면 소수가 아님
    # 전부 나누어 떨어지지 않으면 소수!
    for i in range(2, int(math.sqrt(x) + 1)):
    	if x % i == 0:		
        	return False
    return True	


n = int(input())
lst = list(map(int, input().split()))
cnt = 0

for i in lst:
    if i == 1:
        continue
    if primenumber(i) == True:  # 소수이면 카운트
        cnt += 1
print(cnt)