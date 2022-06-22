import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline

N = int(input())
info = list(map(int, input().split()))
check = [-1] * N
rst = []

rst.append(0)
for i in range(1,N):
    while rst and info[rst[-1]] < info[i]:
        check[rst.pop()] = info[i]
    rst.append(i)

print(*check)