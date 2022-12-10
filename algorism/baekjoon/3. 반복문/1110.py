number = int(input())

count = 0
init = number
while True:
  count += 1
  calc = int(number / 10) + (number % 10)
  number = (number % 10 * 10) + (calc % 10)
  if number == init:
    break

print(count)

# l = True
# count = 0
# init = number
# while l:
#   count += 1
#   calc = int(number / 10) + (number % 10)
#   number = (number % 10 * 10) + (calc % 10)
#   if number == init:
#     l = False

# print(count)