import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    p = list(map(int, input().split()))
    rst = 0
    for i in range(1,N-1):
        if p[i-1] < p[i] < p[i+1] or p[i+1] < p[i] < p[i-1]:
            rst += 1

    print("#{} {}".format(tc, rst))
