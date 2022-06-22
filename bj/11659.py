import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement
input = sys.stdin.readline

N, M = map(int, input().split())
info = list(map(int, input().split()))
check = [0, info[0]]
for i in range(1,N):
    check.append(check[-1]+info[i])

for _ in range(M):
    i, j = map(int, input().split())
    print(check[j]-check[i-1])