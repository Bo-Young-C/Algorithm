n = int(input())        # 설탕 무게

sugar = 0               # 설탕 봉지 개수
while n >= 0:
    if n % 5 == 0:      # 5의 배수이거나 0 이면 설탕 봉지 개수는 무게를 5로 나눈 몫
        sugar += n // 5
        print(sugar)
        break           # 종료

    n -= 3              # 5로 나눠지지 않으면 3킬로그램 봉지 사용
    sugar += 1          # 봉지 개수 카운트

else:                   # 여기까지 왔다면 정확하기 n 킬로그램 만들 수 없음
    print(-1)
