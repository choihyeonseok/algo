import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
from itertools import combinations_with_replacement
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(range(1,N+1))
# print(num_list)

for i in combinations_with_replacement(num_list, M):
    print(*list(i))
    # print(i)
    # tmp = sorted(list(i))
    # if list(i) == tmp:
    #     print(*list(i))
