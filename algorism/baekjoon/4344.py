
case = int(input())

for i in range(case):
  grades = list(map(int, input().split( )))
  n = grades.pop(0)
  total = 0
  for grade in range(n):
    total += grades[grade]
  ave = total / n
  higher = [float(i) for i in grades if i > ave]
  
  higher_ave = round(len(higher) / n * 100, 3)
  print("{:.3f}%".format(higher_ave))

# 다른사람 풀이
  
c = int(input())
for i in range(c):
  score_list = list(map(int,input().split()))
  N = score_list[0]
  del score_list[0]

  sum_list = sum(score_list)
  avg_list = sum_list / N
  M = 0

  for i in score_list:
    if i > avg_list:
      M += 1
  print("{0:.3f}%".format(M/N * 100))


# 다른사람 풀이

n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생 수
    rate = cnt/nums[0] *100
    print(f'{rate:.3f}%')


# 다른사람 풀이


import sys

# 총 케이스 개수
total = int(sys.stdin.readline())
for i in range(total) :
	# 각 케이스 입력(첫 번째 입력값: 해당 케이스의 학생 수)
	case = list(map(int, sys.stdin.readline().split()))
	avg = sum(case[1:]) / case[0]
	# 평균을 넘는 학생 수
	cnt = 0
	for j in case[1:] :
		if j > avg :
			cnt += 1
	print(f'{cnt/case[0] * 100:.3f}%')