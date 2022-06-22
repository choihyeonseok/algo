import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    rst = 0
    for _ in range(N):
        p, x= map(float,input().split())
        rst += p * x

    print("#{}".format(tc), end=" ")
    print("%.6f"%rst)