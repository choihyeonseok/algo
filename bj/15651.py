import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
from itertools import product
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(range(1,N+1))
# print(num_list)

for i in product(num_list, repeat = M):
    print(*list(i))
    # print(i)
    # tmp = sorted(list(i))
    # if list(i) == tmp:
    #     print(*list(i))
