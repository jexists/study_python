import sys

input = sys.stdin.readline
num = int(input())

for i in range(num):
  a, b = map(int, input().split( ))
  print("Case #"+str(i + 1)+":", a + b)
  # print("Case #%d: %d" % (i+1, a + b))
  # print(f'Case #{i}: {a+b}')