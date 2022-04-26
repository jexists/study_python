

# 제어문

# 반복문 (for)

# for 변수 in 반복 가능한 객체:
#   반복하여 실행할 내용
# 반복가능한 객체: list / range

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in a:
    print(i)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

for i in range(11):
    print(i)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# for i in range(처음숫자, 마지막숫자, 증감숫자):
for i in range(1, 10, 2):
    print(i)
# 1
# 3
# 5
# 7
# 9

# for i in range(처음숫자, 마지막숫자, 감소숫자):
for i in range(9, 0, -2):
    print(i)
# 9
# 7
# 5
# 3
# 1

result = 0  # 초기값 지정
for i in range(1, 11, 1):
    # result = result + i
    result += i
print(result)  # 55

for i in range(2, 10, 1):
    print(i)
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# 구구단
for i in range(2, 10, 1):
    for j in range(1, 10, 1):
        # print(i * j)
        print('{} x {} = {}'.format(i, j, i*j))
