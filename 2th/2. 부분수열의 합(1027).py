import sys
import itertools
input = sys.stdin.readline

num, total = map(int,input().split())

lst = list(map(int, input().split()))
count = 0

for i in range(num):
  result = list(itertools.combinations(lst,i+1))
  for i in range(len(result)):
    if sum(result[i]) == total:
      count += 1

print(count)
  