
import math

a, b, c = map(int,input().split( ))

if b >= c:
  print(-1)
else:
  print(math.floor(a/(c-b)) + 1)
  # if c * n > a + (b * n):
  # n > a/(c-b)


# 시간 초과 ===========
# a, b, c = map(int,input().split( ))
# if c < b:
#   print(-1)
# else:
#   for n in range(2100000000):
#     if c * n > a + (b * n):
#       print(n)
#       break