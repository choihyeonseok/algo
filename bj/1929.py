import sys
import math

sys.stdin = open("exam_input.txt")
input = sys.stdin.readline

M, N = map(int, input().split())
N += 1
if M == 1:
    M = 2
tmp = int(math.sqrt(N)) + 1
for i in range(M, N):
    for j in range(2, min(i, tmp)):
        if i % j == 0:
            break
    else:
        print(i, end = "\n")