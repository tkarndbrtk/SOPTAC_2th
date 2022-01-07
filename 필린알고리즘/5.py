
case = int(input())

for i in range(case):
  OX = list(input())
  sum = 0
  sum_sum = 0
  for i in OX:
    if i =='O':
      sum+=1
      sum_sum +=sum
    else:
      sum = 0
  print(sum_sum)