
import sys

input = sys.stdin.readline
num = int(input())
# print(num)

for i in range(num):
  a, b = map(int, input().split( ))
  print(a + b)

