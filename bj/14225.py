import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
check = [0]*sum(S)
# print(S)
# print(check)

for n in range(1, N+1):
    for i in combinations(S, n):
        # print(sum(i), i)
        check[sum(i)-1] += 1

# print(check)

if 0 in check:
    for i in range(sum(S)):
        if check[i] == 0:
            print(i+1)
            break
else:
    print(sum(S)+1)