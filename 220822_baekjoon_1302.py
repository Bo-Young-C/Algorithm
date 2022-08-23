n = int(input())            # 입력받는 책 개수
books = {}                  # 책 리스트
for _ in range(n):
    book = input()
    if book not in books:   # books 에 없으면 새로 넣고  카운트
        books[book] = 1     # 있으면 카운트
    else:
        books[book] += 1

mx = max(books.values())
best = []

for book, count in books.items():
    if count == mx:         # 가장 많이 팔린 책 구하기
        best += [book]

result = sorted(best)[0]
print(result)