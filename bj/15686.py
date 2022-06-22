import sys
from itertools import combinations
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

# 15686 치킨배달

N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]

# for i in range(N):
#     for j in range(N):
#         print(info[i][j], end=" ")
#     print()

home_info = []
chicken_info = []
for i in range(N):
    for j in range(N):
        if info[i][j] == 1:
            home_info.append((i,j))

        if info[i][j] == 2:
            chicken_info.append((i,j))

# print(home_info)
# print(chicken_info)
result = 2147483647
for chicken in combinations(chicken_info, M):
    # print(i)
    rst = 0
    for i in home_info:
        # print(i[0],i[1])
        min_value = N ** 2
        for j in chicken:
            rst_value = abs(i[0] - j[0]) + abs(i[1] - j[1])
            if min_value > rst_value:
                min_value = rst_value
        rst += min_value

    if result > rst:
        result = rst

print(result)