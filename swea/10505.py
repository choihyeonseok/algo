import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    info = list(map(int,input().split()))
    tmp = sum(info) // N
    rst = 0
    for i in info:
        if i <= tmp:
            rst += 1


    print("#{} {}".format(tc,rst))