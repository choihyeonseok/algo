import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    info = list(map(int,input().split()))
    rst = 0
    for i in info:
        if i < 40:
            i = 40
        rst += i
    rst //= 5
    print("#{} {}".format(tc, rst))
