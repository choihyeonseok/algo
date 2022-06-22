import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    scores = list(map(int,input().split()))
    scores.sort(reverse=True)

    rst = 0
    for i in range(K):
        rst += scores[i]

    print("#{} {}".format(tc, rst))
