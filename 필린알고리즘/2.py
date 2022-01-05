import sys
from itertools import combinations
input = sys.stdin.readline
lst = []
for i in range(9):
  lst.append(int(input()))
sum_list = list(combinations(lst,7))
for i in sum_list:
  if sum(i) ==100:
    x= sorted(i)
for i in x:
  print(i)
