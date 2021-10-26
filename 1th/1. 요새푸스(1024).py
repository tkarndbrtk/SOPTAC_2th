

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

lst = [i for i in range(1, n+1)]
order = []
t = k
while 1:
  x = (t-1) %(len(lst))
  order.append(lst.pop(x))
  t = x + k
  if len(lst) ==0:
    break

josephus = ", ".join(str(a) for a in order)
print(f"<{josephus}>")
