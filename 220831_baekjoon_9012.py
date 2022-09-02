T = int(input())

for _ in range(T):
    bracket = list(input())     
    stack = []                      # 빈 스택 생성
    result = 'YES'
    for i in bracket:
        if i == '(':                # 왼쪽 괄호 만나면 스택에 넣기
            stack.append(i)
        else:
            if stack and i == ')':  # 스택에 왼쪽괄호가 존재하고 오른쪽 괄호를 만났을 때
                stack.pop()         # 왼쪽 괄호 제거
            else:
                result = 'NO'       # 빈 스택이면 왼쪽괄호가 나오기도 전에 오른쪽 괄호가 나온것
                break               # 틀린것!
    if stack:                       # 다 끝났는데도 스택이 비어있지 않으면
        result = 'NO'               # 틀린 것!
    print(result)