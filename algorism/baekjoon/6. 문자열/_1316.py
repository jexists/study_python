# 나중에 확인...

number = int(input())

total = 0
for item in range(number):
  word = input()
  prev = ""
  list = []
  for char in word :
    counts=word.count(char)
    if char == prev and counts != 1:
      # print("??")
      list.append(True)
    elif counts == 1:
      # print("??!")
      list.append(True)
    else:
      list.append(False)
    prev = char
    # print(list)

  print(list)
  checkes = [bool for bool in list if bool == False]
  print(checkes)
  if len(checkes) == 0 :
    total += 1


print(total)
