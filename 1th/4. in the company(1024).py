import sys
input = sys.stdin.readline
log_num = int(input())
status = set()
for i in range(log_num):
  name, log = map(str, input().split())
  if log == 'enter':
    status.add(name)
  else:
    status.remove(name)
for i in sorted(status, reverse=True):
  print(i)