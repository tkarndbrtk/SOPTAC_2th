import sys
input = sys.stdin.readline

num = int(input())
lst = []
rank = [1] * num
for _ in range(num):
  w, h = map(int,input().split())
  lst.append((w,h))
for i in range(num):
  for j in range(num):
    if lst[i][0] < lst[j][0] and lst[i][1]<lst[j][1]:
      rank[i] += 1

print(' '.join(str(x) for x in rank))