# n : 자연수, count_num : 빈도수를 구할 숫자
n, count_num = map(int, input().split())

result = 0  # 카운트한 결과

for i in range(1, n+1):
    for num in str(i):  # 문자열로 바꾸고 자릿수 하나씩 추출
        if int(num) == count_num:  # count_num 와 같다면 -> 카운트
            result += 1
print(result)