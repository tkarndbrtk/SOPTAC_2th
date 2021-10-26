import sys
import heapq
input = sys.stdin.readline

lst =[]
total =[]
univ_count = int(input())
for i in range(univ_count):
  money, day = map(int,input().split())
  lst.append((day,money))
sorted_lst = sorted(lst, key = lambda x : x[0])

for i in sorted_lst:
  heapq.heappush(total, i[1])
  if len(total) > i[0]:
    heapq.heappop(total)

print(sum(total))