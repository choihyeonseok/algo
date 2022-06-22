import sys
sys.stdin = open("test_input.txt")
from itertools import permutations
# from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(range(1,N+1))
# print(num_list)

for i in permutations(num_list, M):
    print(*list(i))