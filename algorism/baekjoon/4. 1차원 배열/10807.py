
number = int(input())
list = list(map(int, input().split( )))
integer = int(input())
count = 0
for i in range(number):
  if (list[i] == integer):
    count += 1;
print(count)


# 다른사람 풀이 ==========
N = int(input())
case = list(map(int,input().split()))
v = int(input())

# count : python 리스트 내장 메소드 count() 는 매개변수로 입력된 값이 리스트 안에 몇개 있는지 세어 반환해줍니다.
result = case.count(v)
print(result)