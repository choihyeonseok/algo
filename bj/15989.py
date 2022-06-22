import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
from itertools import combinations_with_replacement
input = sys.stdin.readline

# T = int(input())
# num = [1,2,3]
# for _ in range(T):
#     N = int(input())
#     cnt = 0
#     # print(N)
#     for n in range(1, N+1):
#         for i in combinations_with_replacement(num, n):
#             if sum(i) == N:
#                 cnt += 1
#                 # print(i)
#
#     print(N,cnt)

T = int(input())

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]

for i in range(3, 10001):
    dp[i] += dp[i - 3]

for _ in range(T):
    n = int(input())
    print(dp[n])

