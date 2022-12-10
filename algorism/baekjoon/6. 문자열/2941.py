
# croatia = ["č","ć","dž","đ","lj","nj","š","ž"]
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()

num = 0

for alphabet in croatia:
    # print(alphabet)
    # print(num)
    num += word.count(alphabet)
    word = word.replace(alphabet, " ")
# print(num)
# print(word)
print(num + len(word.replace(" ", "")))


# 참고
croatian = ["c=","c-","dz=","d-","lj","nj","s=","z="]
alpha = input()
length = len(alpha)

for i in croatian:
  length -= alpha.count(i)

print(length)

#참고 2
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(word))