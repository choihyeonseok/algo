import sys
sys.stdin = open("test_input.txt")

T = int(input())

for tc in range(1, T+1):
    p, q = map(float, input().split())
    print(tc, p, q)

    # print()