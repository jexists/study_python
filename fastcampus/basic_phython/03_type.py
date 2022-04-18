
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
