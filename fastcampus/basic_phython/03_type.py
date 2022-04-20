
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
print(str_c + str_d) # helloworld // 문자형 합
print(str_c * 3) # hellohellohello // 문자형 곱
print(str_c,int_a) # hello 1 문자형 숫자형 혼용
# print(str_c + int_a) # ERROR
print(str_c + str(int_a)) # hello1 문자형 숫자형 혼용: 숫자형 -> 문자형 변형
print('str_c {}'.format(int_a)) # hello 1 문자형 숫자형 혼용: format 함수 사용
print('{}월 {}일'.format(5,11)) # 5월 11일
print('{month}월 {day}일'.format(month = 5, day = 11)) # 5월 11일

# 문자형 분해
str_e = 'hello world'
print(str_e.split()) # ['hello', 'world'] // space 기준 분리
str_f = 'joy, happy, sadness'
print(str_f.split(',')) # ['joy', ' happy', ' sadness'] // 기준 분리


# 리스트

list_a = [1, 2, 3, 4, 5]
print(list_a) # [1, 2, 3, 4, 5]
print(type(list_a)) # <class 'list'>

# 리스트내부에 리스트 포함 가능
list_b = [1, [1, 2], [1, [1, 2]]] 
print(list_b[0]) # 1
print(list_b[1][1]) # 2
print(list_b[2][1][0]) # 1

list_c = [1, [2, 3], [4, [5, 6, 7]]] 
print(list_c[0]) # 1
print(list_c[-1]) # [4, [5, 6, 7]]

# 슬라이스
print(list_c[1:]) # [[2, 3], [4, [5, 6, 7]]]
print(list_c[2][1][1:]) # [6, 7]

# 치환
list_d = [1, [2, 3], [4, [5, 6, 7]]] 

list_d[0] = 10
print(list_d) # [10, [2, 3], [4, [5, 6, 7]]]
list_c[2][1][1:] = [60, 70]
print(list_c) # [1, [2, 3], [4, [5, 60, 70]]]
# list_c[2][1][1:] = 50 # ERROR (같은 타입/자료형이여야 함)
list_c[2][1][1:] = [50]
print(list_c) # [1, [2, 3], [4, [5, 50]]]

# 리스트 계산
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b) # [1, 2, 3, 4, 5, 6]

print(a * 2) # [1, 2, 3, 1, 2, 3]

# 내장함수
# append: 뒤에 값 넣기
c = [1, 2, 3]
c.append(4)
print(c) # [1, 2, 3, 4]
d = [1, 2, 3]
d.append([4, 5])
print(d) # [1, 2, 3, [4, 5]]

# pop: 해당 위치 인덱스 삭제
e = [1, 2, 3]
e.pop()
print(e) # [1, 2]
f = [1, 2, 3]
f.pop(1)
print(f) # [1, 3]

# index: 리스트에 인덱스 값 반환
g = [1, 2, 3]
print(a.index(2)) # 1 (인덱스)