
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

word = input()

for i in alphabet:
  print(word.find(i))


# https://betterprogramming.pub/5-ways-to-find-the-index-of-a-substring-in-python-13d5293fc76d


# 참고 ===
word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x))) 