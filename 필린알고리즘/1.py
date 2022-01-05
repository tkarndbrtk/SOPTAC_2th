import sys
input = sys.stdin.readline
A, B = 0, 0
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
lst = []
for i in range(10):
  if lst1[i] > lst2[i]:
    A+=3
    lst.append('A')
  elif lst1[i] < lst2[i]:
    B+=3
    lst.append('B')
  else:
    A+=1
    B+=1
print(A,B)
if A>B:
  print('A')
elif A<B:
  print('B')
else:
  if lst==[]:
    print('D')
  else:
    print(lst[-1])