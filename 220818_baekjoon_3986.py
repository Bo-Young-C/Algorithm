N = int(input())
result = 0              # 테스트케이스를 마치고 난뒤 좋은 단어의 수를 출력할 변수
for _ in range(N):
    s = input()         # 문자열 입력
    stack = []          # 스택
    for i in s:         
        if len(stack) == 0: # 스택이 비어있다면 추가
            stack.append(i)
        else:               # 스택이 비어있지 않다면 비교
            if i == 'A':    # A일때
                if stack[-1] == 'B':    # 스택의 마지막 원소와 비교
                    stack.append(i)     # 다르면 추가, 같으면 스택에서 제거
                elif stack[-1] == 'A':
                    stack.pop()
            elif i == 'B':
                if stack[-1] == 'A':
                    stack.append(i)
                elif stack[-1] == 'B':
                    stack.pop()
    # 스택이 비어있다면 좋은 단어!
    if len(stack) == 0: 
        result += 1
print(result)
