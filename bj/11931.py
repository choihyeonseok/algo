import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement
input = sys.stdin.readline

N = int(input())
rst = []
for _ in range(N):
    n = int(input())
    rst.append(n)

rst.sort(reverse=True)
# print(rst)
for i in rst:
    print(i)