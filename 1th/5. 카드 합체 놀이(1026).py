import sys
import heapq
input = sys.stdin.readline

n, m = map(int,input().split())

card_list = list(map(int, input().split()))

heapq.heapify(card_list)
for _ in range(m):
  a = heapq.heappop(card_list)
  b = heapq.heappop(card_list)
  heapq.heappush(card_list, a+b)
  heapq.heappush(card_list, a+b)
print(sum(card_list))


