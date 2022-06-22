import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

N = int(input())

T_list = []
P_list = []
for _ in range(N):
    T, P = map(int, input().split())
    T_list.append(T)
    P_list.append(P)

dp = [0] * (N+1)
for i in range(N-1,-1,-1):
    if i + T_list[i] <= N:
        dp[i] = max(P_list[i] + dp[i+T_list[i]], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])

