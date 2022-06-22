import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline

L, C = map(int, input().split())
info = list(map(str, input().split()))

info.sort()
for i in combinations(info, L):
    if 'a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i:
        # print(i)
        cnt = 0
        if 'a' in i:
            cnt += 1
        if 'e' in i:
            cnt += 1
        if 'i' in i:
            cnt += 1
        if 'o' in i:
            cnt += 1
        if 'u' in i:
            cnt += 1
        if L - cnt >= 2:
            print(''.join(i))