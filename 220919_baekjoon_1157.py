lst = input().lower()

alphabet = list(set(lst))

cnt = []

for i in alphabet:
    count = lst.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) != 1:
    print('?')
else:
    print(alphabet[(cnt.index(max(cnt)))].upper())