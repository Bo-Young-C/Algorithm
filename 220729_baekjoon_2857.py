people = [] # 입력된 첩보원명을 가진 사람들의 리스트
num = [] # 몇 번째 입력인지 넣을 리스트

for _ in range(5): 
    people.append(input()) # 입력 5번 실행해서 people 리스트에 추가

for i in range(1, 6): 
    if 'FBI' in people[i-1]: # people 리스트에서 원소 하나씩 'FBI' 가 있는지 확인
        num.append(i) # 있으면 번호를 num 리스트에 추가

if len(num) == 0: # num 리스트의 길이가 0 => FBI 요원이 없다면
        print('HE GOT AWAY!') # 옆의 문장 출력

else: # FBI 요원이 있다면
    for j in num: 
        print(j, end=' ') # 번호를 공백으로 구분하여 출력
