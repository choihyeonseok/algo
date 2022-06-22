import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    D, H, M = map(int,input().split())
    rst = M-11 + (H-11)*60 + (D-11)*24*60

    if D == 11:
        if H < 11:
            rst = -1
        elif H == 11:
            if M < 11:
                rst = -1

    print("#{} {}".format(tc, rst))
