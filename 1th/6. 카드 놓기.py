'''
 기존
# 5 4 3 2 1 순서 에서
# 1번이면 맨 위에
# 2번이면 위에서 두번째에
# 3번이면 제일 밑에
# 5 4 3 2 1
# 2 3 3 2 1
# 1 5 2 3 4
'''
'''
역발상
# 1 2 3 4 5
# 1 2 3 3 2 
# 기술
# 1은 제일 밑에 
# 2는 밑에서 두번째 
# 3은 제일 위
# 4 3 2 5 1
'''
import sys
from collections import deque
from typing import Deque
input = sys.stdin.readline

n = int(input())
numbers = [i+1 for i in range(n)]
skill = list(map(int,input().split()))
deq = deque()
reversed_skill = skill[::-1]
for i in range(n):
  if reversed_skill[i] == 1:
    deq.append(numbers[i])
  elif reversed_skill[i] == 2:
    deq.insert(-1,numbers[i])
  else:
    deq.appendleft(numbers[i])

deq.reverse()
print(' '.join(str(x) for x in list(deq)))



