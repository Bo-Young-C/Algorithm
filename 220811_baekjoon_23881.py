N, K = map(int, input().split())    # N : 배열의 크기 K : 교환 횟수
nums = list(map(int, input().split()))  # 배열 A의 원소

count = 0   # 교환 횟수 셀 변수
result = -1 # 교환 횟수가 K보다 작으면 기본값으로 -1 나옴
def selection(arr):
    global count, result    # 글로벌 변수
    # 최대값 찾아 인덱스와 값 저장
    for i in range(N-1, 0, -1):
        maxV = nums[0]
        maxidx = 0
        for j in range(1, i+1):
            if nums[j] > maxV:
                maxV, maxidx = nums[j], j
        # nums[i]와 nums[maxdix] 다름 -> 자리 교환, 카운트
        if nums[i] != nums[maxidx]:
            nums[i], nums[maxidx] = nums[maxidx], nums[i]
            count += 1
        # K번째이면 결과값 반환
        if count == K:
            result = f'{nums[maxidx]} {nums[i]}'
    return result

print(selection(nums))