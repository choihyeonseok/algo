import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_plus = [0] * 10000001
N_minus = [0] * 10000001

for i in N_list:
    if i >= 0:
        N_plus[i] += 1
    else:
        N_minus[i*(-1)] += 1

rst = []
for i in M_list:
    if i >= 0:
        if N_plus[i] != 0:
            rst.append(1)
        else:
            rst.append(0)
    else:
        if N_minus[i*(-1)] != 0:
            rst.append(1)
        else:
            rst.append(0)

print(*rst)