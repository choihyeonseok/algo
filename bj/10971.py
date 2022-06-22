import sys
sys.stdin = open("test_input.txt")
from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

# for i in range(N):
#     for j in range(N):
#         print(W[i][j], end=" ")
#     print()

info = list(range(N))
min_value = 2147483647
for i in permutations(info, N):
    # print(i)
    check = list(i)
    check.append(i[0])
    # print(check)
    rst = 0
    for j in range(N):
        if W[check[j]][check[j+1]] != 0:
            rst += W[check[j]][check[j+1]]
        else:
            rst = 0
            break

    # print(check, rst)
    if rst != 0:
        if min_value > rst:
            min_value = rst

print(min_value)
