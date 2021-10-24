import sys
input = sys.stdin.readline

n = int(input())
height = list(map(int, input().split()))
ans = [0] * n
stack = []
for i in range(len(height)-1,-1,-1):
  if not stack:
    stack.append([i, height[i]])
  else:
    while height[i] > stack[-1][1]:
      target = stack.pop()
      ans[target[0]] = i+1
      if not stack:
        break
    stack.append([i, height[i]])

print(' '.join(str(x) for x in ans))
