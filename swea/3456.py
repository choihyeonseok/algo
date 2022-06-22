import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    a, b, c = map(int,input().split())
    if a == b:
        rst = c
    elif a == c:
        rst = b
    elif b == c:
        rst = a

    print("#{} {}".format(tc, rst))
