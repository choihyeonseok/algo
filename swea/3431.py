import sys

sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    L, U, X = map(int, input().split())

    if L <= X <= U:
        rst = 0
    elif X < L:
        rst = L - X
    elif U < X:
        rst = -1

    print("#{} {}".format(tc, rst))