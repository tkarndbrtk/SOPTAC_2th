import sys

input = sys.stdin.readline

lst =[]
univ_count = int(input())
for i in range(univ_count):
  money, day = map(int,input().split())
  lst.append((day,money))
sorted_lst = sorted(lst, key = lambda x : (x[0], -x[1]))
if univ_count!=0:
  total = sorted_lst[0][1]

for i in range(1,len(sorted_lst)):
  if sorted_lst[i][0] == sorted_lst[i-1][0] and sorted_lst[i][1]<= sorted_lst[i-1][1]:
    continue
  else:
    total+= sorted_lst[i][1]
if univ_count!=0:
  print(total)
else:
  print(0)