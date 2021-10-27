# #@ 6이 윗면, 아랫면에 가지 않게 하는 경우의 수
# A F / B D / C E
# 1층에서의 6의 대응 값 제외 다 가능

import sys
input = sys.stdin.readline

position = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0}
num = int(input())
lst = []
result = []
x = 0
for i in range(num):
  lst_lst = list(map(int,input().split()))
  lst.append(lst_lst)

for i in range(6):
  t = lst[0][i]
  k = lst[0][position[i]]
  lst[0].remove(t)
  lst[0].remove(k)
  print(lst[0])
  sum = max(lst[0])
  lst[0].insert(position[i],k)
  lst[0].insert(i,t)
  print(lst[0])
  for j in range(1, num):
    index_k = lst[j].index(k) ## 3
    t = lst[j][index_k] ## 4
    k = lst[j][position[index_k]] ## 1
    lst[j].remove(t)  ## 4
    lst[j].remove(k) ## 1
    print(lst[j]) ## 3 x 2 x 6 5
    sum += max(lst[j])
    lst[j].insert(position[index_k],k)
    lst[j].insert(index_k,t)
    print(lst[j])
  result.append(sum)
  print('\n')

print(result)