import sys
input = sys.stdin.readline

n = int(input())
height = list(map(int, input().split()))
ans = [0] * n
for i in range(1, len(height)):
  for j in range(i-1,-1, -1):
    if height[i] < height[j]:  
      ans[i] = j+1
      break

print(" ".join(str(x) for x in ans))
