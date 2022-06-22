import sys
sys.stdin = open("exam_input.txt")


dp = [1,1]
N = int(input())
if N == 1:
    rst = 1
elif N == 2:
    rst = 1
else:
    while len(dp) != N:
        dp.append((dp[-1] + dp[-2]))
    rst = dp[-1]
print(rst)