import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    n, m = map(int,input().split())

    print("#{} {} {}".format(tc, 2*m-n, n-m))
