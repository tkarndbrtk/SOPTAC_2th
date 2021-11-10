import sys
input = sys.stdin.readline

T = int(input())


for i in range(T):
    N = int(input())
    lst = []
    test_pass = 1
    for i in range(N):
        x, y = (map(int,input().split()))
        lst.append((x, y))
    lst.sort()
    max = lst[0][1]
    for i in range(1, N):
        if lst[i][1] < max:
            test_pass +=1
            max = lst[i][1]
    print(test_pass)

