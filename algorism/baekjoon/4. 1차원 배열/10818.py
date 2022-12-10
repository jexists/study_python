number = int(input())

list = list(map(int, input().split( )))
min = list[0]
max = list[0]
for i in list:
  if i > max: 
    max = i
  if i < min:
    min = i

print(min, max)


# 다른사람 코드 참고 1 ===================
N = int(input())
array = list(map(int,input().split()))

# 오름차순 정렬
array.sort()
print(array[0],array[-1])

# 다른사람 코드 참고 2 ===================
t = int(input())
item = list(map(int,input().split()))
print(min(item),max(item))