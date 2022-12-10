from collections import Counter

word = input().upper()

counter = Counter(sorted(word))
# print(counter)
count = dict(counter)
list = list(count.values())
# print(max(list(count.values())))
# print(list(count.values()).count(max(list(count.values()))))

if list.count(max(list)) > 1:
  print("?")
else:
  print(max(count, key=count.get))