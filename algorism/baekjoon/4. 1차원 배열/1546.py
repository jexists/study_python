
num = int(input())
grades = list(map(int, input().split( )))

highest = max(grades)
total = 0
for v in grades:
  new = v / highest * 100
  total += new
print(total / len(grades))
    