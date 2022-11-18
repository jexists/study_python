
number = int(input())

for i in range(number):
  times, word = input().split( )
  final = ""
  for i in word:
    final = final + i * int(times)
  print(final)

# https://wikidocs.net/20403

# 참고 
T = int(input())

for i in range(T):
  R,S = input().split()
  R = int(R)
  for j in S:
    print(j * R, end='')
  print()
