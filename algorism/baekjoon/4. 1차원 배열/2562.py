
list = []
for i in range(0, 9):
    num = input()
    list.append(int(num))
# list.sort()
max = max(list)
print(max, list.index(max) + 1)