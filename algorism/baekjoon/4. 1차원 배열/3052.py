

n_list = []
for i in range(0, 10):
  remainder = int(input()) % 42
  n_list.append(remainder)

print(len(list(set(n_list))))


# 다른사람 풀이
arr = []
for i in range(10):
    a = int(input())
    # 중복값이 있는지 확인 후에 리스트에 요소 추가하는 케이스
    if a%42 not in arr:
        arr.append(a % 42)
print(len(arr))