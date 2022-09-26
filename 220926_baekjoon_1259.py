n = input()                 

result = []                     # 결과값 저장할 리스트
while n != '0':                 # '0' 이면 종료
    if n[::-1] == n:            # 팰린드롬이면 yes
        result.append('yes')
    else:                       # 아니면 no
        result.append('no')

    n = input()                 # 다시 입력 받기

for i in result:
    print(i)

