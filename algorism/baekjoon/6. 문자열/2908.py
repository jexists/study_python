

a, b = list(input().split())

a = int("".join(reversed(a)))
b = int("".join(reversed(b)))

if a > b:
  print(a)
else:
  print(b)


# 참고

a, b = input().split()
a = a[::-1]
b = b[::-1]
print(max(a, b))