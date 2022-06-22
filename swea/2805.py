import sys
sys.stdin = open("test_input1.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    info = [list(map(int,input())) for _ in range(N)]
    rst = 0
    for i in range(N):
        for j in range(N):
            if i <= N // 2:
                if N // 2 - i <= j <= N // 2 + i:
                    rst += info[i][j]
            else:
                if N // 2 - (N - i - 1) <= j <= N // 2 + (N - i - 1):
                    rst += info[i][j]
    print("#{} {}".format(tc, rst))
