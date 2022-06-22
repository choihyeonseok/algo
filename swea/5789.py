import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    N, Q = map(int,input().split())
    rst = [0]*N
    for i in range(1,Q+1):
        L, R = map(int,input().split())
        for j in range(L-1,R):
            rst[j] = i

    print("#{}".format(tc),end=" ")
    print(*rst)
