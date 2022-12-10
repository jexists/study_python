# https://www.acmicpc.net/problem/3003

# 1, 1, 2, 2, 2, 8

original_chess = [1, 1, 2, 2, 2, 8]

chess = input().split( )
# print('first =', chess)
chess = [int(num) for num in chess]
# chess2 = list(map(int, chess))

for i in range(len(chess)):
    original_chess[i] = original_chess[i] - chess[i]
    # print(original_chess[i])
# print(str(original_chess).lstrip('[').rstrip(']'))
print(*original_chess, sep=' ')

# ==========
chess = [1, 1, 2, 2, 2, 8]
check = "0 1 2 2 2 7"
result = list(map(int, check.split()))
print(result)
for i in range(len(chess)):
  print(chess[i] - result[i], end=" ")