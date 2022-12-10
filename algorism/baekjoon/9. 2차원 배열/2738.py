
N, M = list(map(int, input().split( )))

A = []
B = []
for item in range(N * 2):
  if item < N:
    A.append(list(map(int, input().split( ))))
  else:
    B.append(list(map(int, input().split( ))))
# print(A)
# print(B)

for a in range(N):
  for b in range(M):
    # if b == M - 1:
    #   print(A[a][b] + B[a][b])
    # else:
      print(A[a][b] + B[a][b], end=' ')


# 참고 코딩 ========
n, m = map(int, input().split())
a, b = [], []

for i in [a, b]:
    for j in range(n):
        i.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]
    print(+a[i])