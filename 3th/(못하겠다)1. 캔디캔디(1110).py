import sys
input = sys.stdin.readline
lst = []
candies, friends = map(int,input().split())
sum = 0

for i in range(friends):
    lst.append(int(input()))
lst.sort(reverse = True)

for i in lst

사탕 30개 5명
8
13
17
4
1
원하는 개수 44 - 30 = 14
그리고 나머지 4개 따로 저장
1
4
8
14
17
첫 놈이 만약 14//5보다 작다면, 그대로 출력


만약 크다면, 14//5분배 나머진 고려 안하고 다 분배 가능 그리고 밑에 추가해서 빼주기
