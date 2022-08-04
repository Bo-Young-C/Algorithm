n = int(input())

penta_dot = 5 # 첫 번째 오각형의 점의 개수
increase = 7 # 1단계에서 2단계로의 점의 증가 개수 : 7
for i in range(1, n):
    # 7, 10, 13, ... => 3씩 increase 가 증가함(등차수열)
    penta_dot += increase 
    increase += 3
print(penta_dot % 45678) # n 번째 오각형의 점의 개수를 45678로 나눈 나머지 출력