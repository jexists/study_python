
# 함수 

num = 101

number = set(range(1, num))
add_number = set()

for i in range(1, num):
    print('currnet i = ' + str(i))
    for j in str(i):
        print('currnet j = ' + str(j))
        i += int(j)
    print('**managed num = ' + str(i))
    add_number.add(i)
    print()



print(number)
print(add_number)
self_number_set = number - add_number

for i in sorted(self_number_set):
    print(i)

