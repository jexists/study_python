a, b = input().split( )
list = map(int, input().split( ))

# final = ""
# for index, item in enumerate(list):
#   if int(item) < int(b):
#     final += str(item) + " "
# print(final)

for i in list:
  if i < int(b):
    print(i, end=' ')