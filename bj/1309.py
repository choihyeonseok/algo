import sys
sys.stdin = open("exam_input.txt")
input = sys.stdin.readline

N = int(input())

tmp1 = 3
tmp2 = 7
cnt = 2
if N >= 3:
    while cnt != N:
        rst = 2*tmp2 + tmp1
        tmp1 = tmp2
        tmp2 = rst
        cnt += 1
else:
    if N == 1:
        rst = 3
    if N == 2:
        rst = 7

print(rst % 9901)