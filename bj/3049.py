import sys

sys.stdin = open("test_input.txt")
input = sys.stdin.readline

N = int(input())

if N < 4:
    rst = 0

else:
    rst = 1
    for i in range(N-4):
        rst *= (N-i)/(N-i-4)

print(int(rst+0.5))