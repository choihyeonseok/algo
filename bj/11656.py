import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline

S = input().rstrip()
rst = []
for i in range(len(S)):
    # print(S[i:],i)
    rst.append(S[i:])

rst.sort()
# print(rst)
for i in rst:
    print(i)