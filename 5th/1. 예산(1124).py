import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))
new_list = []
m = int(input()) # 
lst.sort()
for i in range(len(lst)):
  if(len(new_list)!=0): # ! sort를 했기 떼문에, 전 index에서 초과했다면 그 이후는 다 초과한 값들
    new_list.append(lst[i])
  elif (lst[i] <= (m/(len(lst)-i))): # ! 평균값보다 작다면, 통과
    m -= lst[i]
  else:
    new_list.append(lst[i]) # ! 평균값을 초과한다면 새로운 리스트에 추가합니다
if (len(new_list) ==0):
  print(max(lst))
else:
  print(int(m/len(new_list)))
