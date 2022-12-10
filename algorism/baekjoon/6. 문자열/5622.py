

dial = [[],["A","B","C"],["D","E","F"],["G","H","I"],["J","K","L"],["M","N","O"],["P","Q","R","S"],["T","U","V"],["W","X","Y","Z"]]
word = input()

def deep_index(lst, w):
    return [i for (i, sub) in enumerate(lst) if w in sub]

total = 0
for i in list(word):
  total += 1
  total += deep_index(dial, i)[0] + 1
print(total)    

# 참고한 링크: https://stackoverflow.com/questions/15233767/how-do-i-get-index-of-list-in-list