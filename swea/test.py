import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline


T = int(input())
for tc in range(1,T+1):
    # N, K = map(int,input().split())
    N_list = list(map(str,input().split()))
    rst = 0

    print("#{} {}".format(tc, rst))
