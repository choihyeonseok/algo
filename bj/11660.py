import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + info[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    tmp1 = dp[x1-1][y2] + dp[x2][y1-1] - dp[x1-1][y1-1]
    tmp2 = dp[x2][y2]

    print(tmp2-tmp1)

# for _ in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#
#     tmp2 = dp[x2][y2]
#     tmp1 = dp[x1-1][y2] + dp[x2][y1-1] - dp[x1-1][y1-1]
#
#     print(tmp2-tmp1)
