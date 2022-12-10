# def solve(a: list) -> int

def solve(a: list):
  ans = 0
  for i in range(len(a)):
    ans = ans + a[i]
  return ans


def solve(a):
  ans = 0
  for i in range(len(a)):
    ans += a[i]
  return ans

def solve(a):
  return sum(a)

  
print(solve(list(map(int, input().split( )))))