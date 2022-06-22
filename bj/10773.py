import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline

K = int(input())
rst = []
for _ in range(K):
    N = int(input())
    if N != 0:
        rst.append(N)
    else:
        rst.pop(-1)

print(sum(rst))
