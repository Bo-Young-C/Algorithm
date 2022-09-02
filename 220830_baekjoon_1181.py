# 시간초과로 인해 sort 사용...
n = int(input())

words = [input() for _ in range(n)]
words1 = list(set(words))           # 중복 제거
words1.sort(key=lambda word: (len(word), word))     # 길이순으로 정렬

for i in words1:
    print(i)

# 시간초과가 뜨지만 sort를 쓰지 않고 버블정렬로 푼 코드!
# n = int(input())

# words = [input() for _ in range(n)]
# j_ord = 0
# j1_ord = 0
# for i in range(n-1, 0, -1):
#     for j in range(i):      
#         if len(words[j]) > len(words[j+1]):
#             words[j], words[j+1] = words[j+1], words[j]
#         elif len(words[j]) == len(words[j+1]):
#             for k in words[j]:
#                 j_ord += ord(k)
#             for k in words[j+1]:
#                 j1_ord += ord(k)
#             if j_ord > j1_ord:
#                 words[j], words[j+1] = words[j+1], words[j]
# sorted_words = []
# for i in words:
#     if i not in sorted_words:
#         sorted_words.append(i)
# for i in sorted_words:
#     print(i)