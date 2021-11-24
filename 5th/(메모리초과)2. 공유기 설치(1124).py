import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
lst = []
substract = []
for i in range(n):
  lst.append(int(input()))

lst.sort(reverse=True)
comb_list = list(combinations(lst, m))

for i in comb_list:
  substract.append(min(i[0]-i[1],i[1]-i[2]))
print(min(substract))


1 2 4 8 9

start 1, end 9-1 = 8

mid = (1+8)/2 4

count = 1
cur_house = 1
2 - 1은 mid보다 작음
...
8-1은 mid보다 큼
count = 2, cur_house = 8
9-8은 mid보다 작음
끝

count = 2, C는 3이니까 해당 안돼

end = 4 - 1 = 3

start 1, end = 3

다음 while문

mid = 2

cur_house = 1
2 - 1 은 mid보다 작음
..
4-1 은 mid보다 큼
count = 2
cur_house = 4
8 - 4 는 mid보다 작음
count = 3
cur_house = 8

끝

count = C이므로
start = 2+1,
answer = 2