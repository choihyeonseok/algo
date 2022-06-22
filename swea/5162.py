import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    # 현미가격, 단호박가격, 현재금액
    A, B, C = map(int,input().split())
    rst = 0

    if A < B:
        rst += C // A
    else:
        rst += C // B

    print("#{} {}".format(tc, rst))