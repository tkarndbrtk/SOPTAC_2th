time = int(input())
for _ in range(time):
  k = int(input())
  n = int(input())
  live = [ i for i in range(1, n+1)]
  for ___ in range(k):
    for j in range(1,n):
      live[j] += live[j-1]
  print(live[-1])