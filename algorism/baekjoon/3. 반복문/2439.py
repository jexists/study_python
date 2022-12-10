
number = int(input())

for i in range(number):
  print(" " * (number - (i + 1)) + "*" * (i + 1))


# num2 = number
# for i in range(number + 1):
#   final= " " * (num2) + "*" * (number - num2)
#   num2 = num2 - 1
#   if (i != 0):
#     print(final)