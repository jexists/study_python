
# 1부터 10까지 삽입
a = []
for i in range(1, 11, 1):
    a.append(i)
print(a)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = [i for i in range(1, 11, 1)]
print(a)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 1부터 10까지의 제곱의 값 삽입
a = []
for i in range(1, 11, 1):
    a.append(i ** 2)
print(a)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

a = [i ** 2 for i in range(1, 11, 1)]
print(a)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


a = [90, 35, 45, 70, 82, 100]
result = [i for i in a]
print(result)
# [90, 35, 45, 70, 82, 100]
a = [90, 35, 45, 70, 82, 100]

# 80이상만
result = [i for i in a if i >= 80]
print(result)
# [90, 82, 100]