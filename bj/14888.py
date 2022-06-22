import sys
sys.stdin = open("test_input.txt")
from itertools import permutations
input = sys.stdin.readline

N = int(input())
N_list = list(map(int,input().split()))
info_list = list(map(int, input().split()))
info = []
if info_list[0] != 0:
    info += ['+']*info_list[0]

if info_list[1] != 0:
    info += ['-']*info_list[1]

if info_list[2] != 0:
    info += ['*']*info_list[2]

if info_list[3] != 0:
    info += ['//']*info_list[3]

# print(info, '입력')

rst_max_value = -2147483647
rst_min_value = 2147483647
for i in permutations(info, len(info)):
    # print(i)
    rst = 0
    for j in range(N):
        if j == 0:
            rst = N_list[j]
        else:
            if i[j-1] == '+':
                rst += N_list[j]
            if i[j-1] == '-':
                rst -= N_list[j]
            if i[j-1] == '*':
                rst *= N_list[j]
            if i[j-1] == '//':
                rst = int(rst / N_list[j])

    # print(i, rst)

    if rst_min_value > rst:
        rst_min_value = rst
    if rst_max_value < rst:
        rst_max_value = rst

print(rst_max_value)
print(rst_min_value)

