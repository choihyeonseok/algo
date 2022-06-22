import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
input = sys.stdin.readline

N, K = map(int, input().split())
info = list(map(int, input().split()))

for i in range(1, N):
    info[i] += info[i-1]

rst = info[K-1]
for i in range(K+1, N):
    rst = max(rst, info[i] - info[i-K])

print(rst)