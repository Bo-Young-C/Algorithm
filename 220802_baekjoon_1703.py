while 1:
    list_input = list(map(int, input().split())) 
    leaf = 1 #구하고자 하는 나뭇잎 개수이 들어갈 변수
    if list_input[0] == 0: #0을 입력받으면 while문 종료
        break

    for i in range(1, len(list_input), 2):
        leaf = leaf * list_input[i] - list_input[i+1]
    print(leaf)