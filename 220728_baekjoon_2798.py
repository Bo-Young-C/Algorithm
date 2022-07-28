N, M = map(int, input().split()) # 입력값을 공백으로 나누어 각각 N(카드 개수), M(최대한 가깝게 만들어아 하는 카드의 합)에 할당
card = list(map(int, input().split())) # 입력값을 공백으로 나누고 리스트로 만들기

three_card_sum = 0 # 세 카드의 숫자의 합을 저장할 변수 생성

# 브루트 포스
for i in range(N): 
    for j in range(i+1, N): 
        for k in range(j+1, N):
            if card[i] + card[j] + card[k] > M: # 세 카드의 합이 M 보다 크면 다시 반복(하나씩 다 비교)
                continue
            else:
                # M 보다 작으면, three_card_sum 변수와 비교해서 둘 중에 큰 값을 three_card_sum 에 넣어준다.
                three_card_sum = max(three_card_sum, card[i] + card[j] + card[k])
                
print(three_card_sum) # M 을 넘지 않으면서 가장 가까운 합을 출력