# import

# → 불러오겠다.

from calculator import plus
from math import fsum as total_sum
from math import ceil, fsum
import math
from ex_module import good_morning, good_afternoon
import ex_module
import random


# import random

numbers = [1, 2, 3, 4, 5]

rand_numbers = random.sample(numbers, 3)

print(rand_numbers)  # [1, 3, 4]

# 로또 함수


lotto_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
              23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]

lotto = random.sample(lotto_nums, 6)
lotto.sort()
print(lotto.sort())  # RETRUN 없음 = None
print(lotto)  # [4, 10, 17, 22, 27, 41]

lotto_random = random.sample(range(1, 46), 6)
lotto_random.sort()
print(lotto_random)  # [5, 10, 26, 38, 40, 43]


print(sorted(random.sample(range(1, 46), 6)))
# sort => None
# sorted => Return


# 직접 모듈


# import ex_module
# 내장된 모듈(built-in) -> 직접된모듈
# 없는 모듈을 가져오면 ERROR

ex_module.good_morning()  # good morning
ex_module.good_afternoon()  # good afternoon

# from ex_module import good_morning, good_afternoon

good_morning()  # good morning
good_afternoon()  # good afternoon

## import module

# - import : python 안에 내재되어 있는 modules를 가져오는 것. (함수들을)
# - 모든 함수를 import 하는 것은 비효율적
#
#     →because 사용하지 않는 것들도 가져오기 때문

# - 쓸 것만 import

# math — Mathematical functions

# [math - Mathematical functions - Python 3.9.4 documentation](https://docs.python.org/3/library/math.html)


# import math
# 비추천 - 모든 math에 관련된 파일을 가져오기때문

print(math.ceil(1.2))  # 2 올림
print(math.fabs(-1.2))  # 1.2 절대값

# from math import ceil, fsum

print(ceil(1.2))  # 2 올림
print(fsum([1, 2, 3, 4, 5, 6, 7]))  # 28.0

# from math import fsum as total_sum

print(total_sum([1, 2, 3, 4, 5, 6, 7]))  # 28.0

# calculator.py


def plus(a, b):
    return a + b

# main.py


# from calculator import plus
# calculator.py 파일명만 작성

print(plus(1, 2))  # 3


# datetime — Basic date and time types : 자주쓰는 모듈
# [datetime - Basic date and time types - Python 3.9.4 documentation](https://docs.python.org/3/library/datetime.html)

# CSV File Reading and Writing
# [csv - CSV File Reading and Writing - Python 3.9.4 documentation](https://docs.python.org/3/library/csv.html)

# json — JSON encoder and decoder
# [json - JSON encoder and decoder - Python 3.9.4 documentation](https://docs.python.org/3/library/json.html)
