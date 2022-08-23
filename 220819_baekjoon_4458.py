# 리프레시겸 쉬운 문제 풀기...
n = int(input())                
for i in range(n):
    s = str(input())            # 하나씩 입력받고 첫 글자 대문자로 변환
    print(s[0].upper()+s[1:])