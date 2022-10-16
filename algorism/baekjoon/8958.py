
number = int(input())

for i in range(number):
  # case = [(i) for i in input()]
  case = list(input())
  grade = 0
  result = 0
  for item in case:
    if item == "O":
      grade += 1
      result += grade
    else:
      grade = 0
  print(result)