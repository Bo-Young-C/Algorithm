def primenumber(num):       # 소수를 구하는 함수
    if num == 1:            # 1은 소수 아님
        return
    else:
        # 2부터 제곱근까지 순회
        for j in range(2, int(num**0.5)+1):
            # 떨어진다면 소수아님 -> 종료
            if num % j == 0:
                return
        # 여기까지 왔다면 소수! -> 결과 리스트에 추가 후 종료
        result.append(num)
        return


n, m = map(int, input().split())
result = []
# n 부터 m까지 소수인지 확인
for i in range(n, m+1):
    primenumber(i)
for j in result:
    print(j)