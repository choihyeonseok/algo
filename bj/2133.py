import sys
sys.stdin = open("exam_input.txt")

N = int(input())
dp = [3,11] + [0]*(N-2)
if N % 2 == 1:
    rst = 0
else:
    for i in range(2,N//2):
        # print(i)
        dp[i] = 4*dp[i-1] - dp[i-2]
    rst = dp[N//2-1]
print(rst)
# print(dp)