import sys
sys.stdin = open("exam_input.txt")

dp = [1,2]
N = int(input())
if N == 1:
    rst = 1
elif N == 2:
    rst = 2
else:
    while len(dp) != N:
        dp.append((dp[-1] + dp[-2]) % 10007)
    rst = dp[-1]
print(rst)