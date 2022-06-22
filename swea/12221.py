import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    A, B = map(int,input().split())
    rst = A * B
    if A >= 10 or B >= 10:
        rst = -1
    print("#{} {}".format(tc,rst))