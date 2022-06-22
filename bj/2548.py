import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
input = sys.stdin.readline

N = int(input())
info = list(map(int, input().split()))

min_value = 2147483647
min_list = []
for i in info:
    tmp = 0
    for j in info:
        tmp += abs(i-j)

    if min_value > tmp:
        min_value = tmp

    min_list.append((tmp, i))

# print(min_list)
min_list.sort()
# print(min_list)
print(min_list[0][1])



