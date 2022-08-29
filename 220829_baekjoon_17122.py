T = int(input())

arr1 = [[0]*8 for _ in range(8)]                # chess 2차원 배열
arr2 = [0]*65                                   # chess 1차원 배열
for _ in range(T):
    for i in range(8):
        for j in range(8):
            if i % 2 == 0 and j % 2 == 0:       # 행이 짝수이고, 열이 짝수이면 -> 1(검정)
                arr1[i][j] = 1
            elif i % 2 == 1 and j % 2 == 1:     # 행이 홀수이고, 열이 홀수이면 -> 1(검정)
                arr1[i][j] = 1
    for i in range(1, 65):                      # arr 의 1~65 번을 돌면서 흑백 칠해주기
        if i % 8 != 0:                          # 8로 나누어떨어지지 않으면
            if (i // 8)%2 == 0:                 # 8로 나눈 몫이 짝수이고, 홀수이면 검정 칠해주기
                if i % 2 == 1:
                    arr2[i] = 1
            else:                               # 8로 나눈 몫이 홀수이고, 짝수이면 검정 칠해주기
                if i % 2 == 0:
                    arr2[i] = 1
        else:                                   # 8로 나누어떨어지고, 8로 나눈 몫이 짝수이면 검정 칠해주기
            if (i // 8)%2 == 0:
                arr2[i] = 1   
    a, b = input().split()
    c = ord(a[0])-65                            # 알파벳을 인덱스로 변환
    d = int(b)
    if arr1[c][int(a[1])-1] == arr2[d]:         # 같은 색인지 확인
        ans = 'YES'         
    else:
        ans = 'NO'
    print(ans)