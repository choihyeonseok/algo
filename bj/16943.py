import sys
sys.stdin = open("test_input.txt")
from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline

A, B = map(str, input().split())
B = int(B)
C = -1

rst = []
for i in permutations(A, len(A)):
    # print(i)
    rst.append(''.join(i))
# print(rst1)

for i in rst:
    start = i[0]
    if i[0] != '0':
        if B > int(i):
            C = max(C, int(i))

print(C)