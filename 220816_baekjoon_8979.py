N, K = map(int, input().split())

medals = [[] for _ in range(N+1)]
for _ in range(N):
    nation, gold, silver, bronze = map(int, input().split())
    medals[nation] = [gold, silver, bronze]
gold_k, silver_k, bronze_k = medals[K]

count = 1
# k의 금, 은, 동과 다른 나라들의 금, 은, 동 비교
for i in range(1, N+1):
    if gold_k < medals[i][0]:   # 먼저 금 비교
        count += 1  # k 보다 크면 카운트
    elif gold_k == medals[i][0]:    # 금이 같으면 다음 은 비교
        if silver_k < medals[i][1]:
            count += 1  # k 보다 크면 카운트
        elif silver_k == medals[i][1]:  # 은이 같으면 다음 동 비교
            if bronze_k < medals[i][2]:
                count += 1  # k 보다 크면 카운트
print(count)
