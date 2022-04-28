# 함수

# 함수를 만드는 이유
# 같은 작업을 여러번 반복

# 생성방법
# def 함수명(인풋 값):
#   실행 내용

from unittest import result


def function1(x):
    print(x + 1)


function1(1)  # 2

# 반환값 받기


def function2(x):
    return x + 1


a = function2(1)
print(a)  # 2

# 여러개 반환값 받기


def function3(x):
    result1 = x + 1
    result2 = x + 2
    return result1, result2


b, c = function3(1)
print(b, c)  # 2 3


def function4(x):
    for i in x:
        print(i)


a = [1, 3, 5, 7, 4, 'd', 2, 60]
function4(a)
# 1
# 3
# 5
# 7
# 4
# d
# 2
# 60

# arguments 사용해서 함수 (*)
def function5(*args):
    for i in args:
        print(i)

function5(1, 3, 5, 7, 4, 'd', 2, 60)
# 1
# 3
# 5
# 7
# 4
# d
# 2
# 60