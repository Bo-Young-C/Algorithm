arr = [int(input()) for _ in range(9)]

# 버블 정렬로 오름차순 정렬
for i in range(8):
    for j in range(8-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

ssum = 0
# 아홉 명의 키 합
for i in range(9):
    ssum += arr[i]
# 아홉 명의 키 합 - 100(일곱난쟁이 키의 합) = 가짜 난쟁이의 키의 합
ssum -= 100 
s = 0
e = 8
while s != e: 
    if arr[s] + arr[e] == ssum: # 두 합이 가짜 난쟁이의 합과 같다면
        # 배열에서 제거 후 반복문 종료
        del arr[e], arr[s] 
        break
    elif arr[s] + arr[e] > ssum:
        e -= 1
    else:
        s += 1

for i in range(7): # 일곱난쟁이 출력
    print(arr[i])

