n, w, h = map(int, input().split()) # n : 성냥개수, w : 상자 가로길이, h : 상자 세로길이

result = [] # 결과값을 넣을 리스트 생성
for i in range(n): 
    matches = int(input()) # 한 줄씩 성냥 길이 입력
    # 성냥 길이 <= 상자 가로 or 성냥 길이 <= 상자 세로 or 성냥 길이 <= 상자 대각선 ==> 상자에 들어갈수 있음
    if matches <= w or matches <= h or matches <= (w**2 + h**2)**(1/2):
        result.append('DA') # 들어갈 수 있으면 DA 추가

    else:
        result.append('NE') # 없으면 NE 추가
for j in result:
    print(j) # 한줄씩 결과값 출력