import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    N_info = list(range(1,N+1))
    info = list(map(int, input().split()))

    print("#{}".format(tc),end=" ")
    for i in N_info:
        if i not in info:
            print(i,end=" ")
    print()
    # print("#{} {}".format(tc, rst))
