N = int(input()) # N : 수의 개수 

numbers = [] # 입력된 수들을 넣을 리스트 생성
for i in range(N):
    numbers.append(int(input())) # 리스트에 넣기
sorted_numbers = sorted(numbers) # 오름차순으로 정렬
for number in sorted_numbers: 
    print(number)