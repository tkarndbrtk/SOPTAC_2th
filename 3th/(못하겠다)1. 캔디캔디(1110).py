import sys
input = sys.stdin.readline
lst = []
M, N = map(int,input().split())
for i in range(N):
    lst.append(int(input()))
lst.sort()
give_me_a_candies = sum(lst) - M # 필요 캔디 - 가진 캔디 = 못받은 캔디
ans = 0

for i in range(N):
    # 가장 분노가 최소인 지점 => 각 사람들이 못 받은 캔디 개수가 같을 때
    # vacant는 분노가 최소가 되게 하는 한 사람이 못 받은 캔디의 개수
    vacant = give_me_a_candies // ( N - i ) 

    # 하지만 한 친구가 필요로 한 사탕 개수가 vacant보다 작다면 예외처리를 해줘야 함 
    if lst[i] >= vacant:
        given = vacant
        ans += given * given
    else:
        given = lst[i]
        ans += given * given
    give_me_a_candies -= given

print(ans%(2**64))


