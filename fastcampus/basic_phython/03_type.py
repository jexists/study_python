
# 숫자형

int_a = 1
int_b = -1
float_a = 0.1
float_b = 0.0
float_c = -0.1
float_d = -0.

print(type(int_a))  # <class 'int'>
print(type(int_b))  # <class 'int'>
print(type(float_a))  # <class 'float'>
print(type(float_b))  # <class 'float'>
print(type(float_c))  # <class 'float'>
print(type(float_d))  # <class 'float'>
# int + float = float
print(type(int_a + float_d))  # <class 'float'>


str_a = 'hello world'
str_b = "hello world"
print(type(str_a))  # <class 'str'>
print(type(str_b))  # <class 'str'>
print(str_a[0])  # h // 첫번째 문자 출력
print(str_a[-1])  # d // 마지막 문자 출력
print(str_a)  # hello world // 전체 출력
print(str_a[:])  # hello world // 전체 출력
print(str_a[2:8])  # llo wo // 원하는 부분 출력 [이상:미만]
print(str_a[:4])  # hell // 처음부터 원하는 부분 출력
print(str_a[4:])  # o world // 원하는 부분부터 마지막 출력
print(str_a[-4:])  # orld // 뒤에서 원하는 부분부터 마지막 출력
print(str_a[:-4])  # hello w // 처음부터 뒤에서 원하는 부분부터 마지막 출력

# 문자형 계산
str_c = 'hello'
str_d = 'world'
print(str_c + str_d)  # helloworld // 문자형 합
print(str_c * 3)  # hellohellohello // 문자형 곱
print(str_c, int_a)  # hello 1 문자형 숫자형 혼용
# print(str_c + int_a) # ERROR
print(str_c + str(int_a))  # hello1 문자형 숫자형 혼용: 숫자형 -> 문자형 변형
print('str_c {}'.format(int_a))  # hello 1 문자형 숫자형 혼용: format 함수 사용
print('{}월 {}일'.format(5, 11))  # 5월 11일
print('{month}월 {day}일'.format(month=5, day=11))  # 5월 11일

# 문자형 분해
str_e = 'hello world'
print(str_e.split())  # ['hello', 'world'] // space 기준 분리
str_f = 'joy, happy, sadness'
print(str_f.split(','))  # ['joy', ' happy', ' sadness'] // 기준 분리


# 리스트

list_a = [1, 2, 3, 4, 5]
print(list_a)  # [1, 2, 3, 4, 5]
print(type(list_a))  # <class 'list'>

# 리스트내부에 리스트 포함 가능
list_b = [1, [1, 2], [1, [1, 2]]]
print(list_b[0])  # 1
print(list_b[1][1])  # 2
print(list_b[2][1][0])  # 1

list_c = [1, [2, 3], [4, [5, 6, 7]]]
print(list_c[0])  # 1
print(list_c[-1])  # [4, [5, 6, 7]]

# 슬라이스
print(list_c[1:])  # [[2, 3], [4, [5, 6, 7]]]
print(list_c[2][1][1:])  # [6, 7]

# 치환
list_d = [1, [2, 3], [4, [5, 6, 7]]]

list_d[0] = 10
print(list_d)  # [10, [2, 3], [4, [5, 6, 7]]]
list_c[2][1][1:] = [60, 70]
print(list_c)  # [1, [2, 3], [4, [5, 60, 70]]]
# list_c[2][1][1:] = 50 # ERROR (같은 타입/자료형이여야 함)
list_c[2][1][1:] = [50]
print(list_c)  # [1, [2, 3], [4, [5, 50]]]

# 리스트 계산
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)  # [1, 2, 3, 4, 5, 6]

print(a * 2)  # [1, 2, 3, 1, 2, 3]

# 내장함수
# append: 뒤에 값 넣기
c = [1, 2, 3]
c.append(4)
print(c)  # [1, 2, 3, 4]
d = [1, 2, 3]
d.append([4, 5])
print(d)  # [1, 2, 3, [4, 5]]

# pop: 해당 위치 인덱스 삭제
e = [1, 2, 3]
e.pop()
print(e)  # [1, 2]
f = [1, 2, 3]
f.pop(1)
print(f)  # [1, 3]

# index: 리스트에 인덱스 값 반환
g = [1, 2, 3]
print(a.index(2))  # 1 (인덱스)

# 튜플
tuple_a = (1, 2, 3)
print(tuple_a)  # (1, 2, 3)
print(type(tuple_a))  # <class 'tuple'>
print(tuple_a[1])  # 2
print(tuple_a[:2])  # (1, 2)
# tuple_a[2] = 0 # ERROR 리스트 튜플 차이: 치환 (가능: 리스트 / 불가능: 튜플)
# 바뀌면 안되는 값들 사용

# 치환 제한 & 생성은 가능
tuple_b = (1, 2, 3)
tuple_c = (4, 5, 6)
print(tuple_b + tuple_c)  # (1, 2, 3, 4, 5, 6)
print(tuple_b * 2)  # (1, 2, 3, 1, 2, 3)


# 딕셔너리 (dict)
# key와 value로 구성

dict_a = {'사과': 'apple', '오렌지': 'orange'}
print(dict_a)  # {'사과': 'apple', '오렌지': 'orange'}
print(type(dict_a))  # <class 'dict'>

# 하나의 key에 여러개의 value로도 구성이 가능
dict_b = {'fruit': ['apple', 'orange'], 'vegetable': 'tomato'}
print(dict_b)  # {'fruit': ['apple', 'orange'], 'vegetable': 'tomato'}

print(dict_b.keys())  # dict_keys(['fruit', 'vegetable'])

key = dict_b.keys()

print(type(key))  # <class 'dict_keys'>

# print(key[0]) # ERROR (list type 변환 필요)

key2 = list(key)
print(type(key2))  # <class 'list'>
print(key2[0])  # fruit

value = dict_b.values()
print(value)  # dict_values([['apple', 'orange'], 'tomato'])

# print(value[0]) # ERROR
value2 = list(value)
print(type(value2))  # <class 'list'>
print(value2[0])  # ['apple', 'orange']

# 요소 추가
dict_c = {'fruit': ['apple', 'orange'], 'vegetable': 'tomato'}
dict_c['meat'] = 'beef'
# {'fruit': ['apple', 'orange'], 'vegetable': 'tomato', 'meat': 'beef'}
print(dict_c)

# 요소 삭제
dict_d = {'fruit': ['apple', 'orange'], 'vegetable': 'tomato'}
del dict_d['vegetable']
print(dict_d)  # {'fruit': ['apple', 'orange']}

# SET 셋
set_a = set([1, 2, 3])
print(set_a)  # {1, 2, 3}
print(type(set_a))  # <class 'set'>

set_b = set({1, 2, 3})
print(set_b)  # {1, 2, 3}
print(type(set_b))  # <class 'set'>

set_c = set((1, 2, 3))
print(set_c)  # {1, 2, 3}
print(type(set_c))  # <class 'set'>

# 특징: 중복제거
set_d = set([1, 1, 2, 3, 3, 4])
print(set_d)  # {1, 2, 3, 4} (중복제거)

# 특징: 순서없음 (index 없음)
set_e = set([4, 4, 3, 2, 1, 'a', 'b', 'a'])
print(set_e) # {1, 2, 3, 4, 'b', 'a'}
# print(set_e[0]) # ERROR => 타입변환 후 찾기

type_e = list(set_e)
print(type_e) # [1, 2, 3, 4, 'b', 'a']
print(type_e[0]) # 1


# 집합
set_f = set([1,2,3])
set_g = set([3,4,5])

# 합집합
set_h = set_f.union(set_g)
print(set_h) # {1, 2, 3, 4, 5}

# 교집합
set_i = set_f.intersection(set_g)
print(set_i) # {3}

# 차집합
set_j = set_f.difference(set_g)
print(set_j) # {1, 2}
set_k = set_g.difference(set_f)
print(set_k) # {4, 5}