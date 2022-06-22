import sys
from itertools import combinations
sys.stdin = open("test_input.txt")

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


# for i in range(N):
#     for j in range(N):
#         print(arr[i][j], end=" ")
#     print()

min_value = 2147483647
for i in combinations(list(range(1,N+1)), N//2):
    start = []
    link = list(range(1,N+1))
    for j in i:
        start.append(j)
        link.remove(j)

    start_sum = 0
    for k in start:
        for l in start:
            if k != l:
                start_sum += arr[k-1][l-1]
    # print(start, start_sum)

    link_sum = 0
    for k in link:
        for l in link:
            if k != l:
                link_sum += arr[k-1][l-1]
    # print(link, link_sum)
    rst = abs(start_sum-link_sum)
    # print(rst)

    if min_value > rst:
        min_value = rst

print(min_value)