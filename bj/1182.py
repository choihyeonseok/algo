import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement
input = sys.stdin.readline

N, S = map(int, input().split())
info = list(map(int, input().split()))

cnt = 0
for n in range(1, N+1):
    for i in combinations(info, n):
        # print(sum(i))
        if sum(i) == S:
            cnt += 1

print(cnt)