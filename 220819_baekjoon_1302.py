import sys
n = int(input())
book = dict()
for _ in range(n):
    name = input()
    if name in book:
        book[name] += 1
    else:
        book[name] = 1
max = 0
    sbook = book.items()
for i in sbook:
    if (sbook[i]) > max:
        max = sbook[i]
        maxi = i
print(maxi)