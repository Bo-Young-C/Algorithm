
result = [] # 결과값을 넣을 리스트 생성
while True:
    a, b, c = map(int, input().split()) # 세 변을 입력
    sorted_number = sorted([a, b, c]) # 세 변을 크기순으로 정렬
    if a == 0 and b == 0 and c == 0: # 만약 0 0 0이면 while 문 종료
        break
    # 가장 긴 변의 길이의 제곱 = 나머지 두 변의 제곱의 합 => 직각삼각형
    elif int(sorted_number[2])**2 == int(sorted_number[0])**2 + int(sorted_number[1])**2:
        result.append('right')
    else:
        result.append('wrong')
for i in range(len(result)): # 리스트 원소 하나씩 출력
    print(result[i])
    

        
