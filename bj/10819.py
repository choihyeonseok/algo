import sys
sys.stdin = open("test_input.txt")
from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline
N = int(input())
info = list(map(int, input().split()))

max_value = 0
for i in permutations(info, N):
    # print(i)
    rst = 0
    for j in range(N-1):
        rst += abs(i[j]-i[j+1])

    if max_value < rst:
        max_value = rst

print(max_value)
