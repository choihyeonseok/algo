import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline

# N = int(input())
# X = list(map(int, input().split()))
#
# # print(X)
# rst = []
# for i in X:
#     cnt = 0
#     cnt_list = []
#     for j in X:
#         if i > j and j not in cnt_list:
#             cnt += 1
#             cnt_list.append(j)
#
#     rst.append(cnt)
# print(*rst)

N = int(input())
X = list(map(int, input().split()))

X_new = sorted(list(set(X)))
rst = {X_new[i] : i for i in range(len(X_new))}
# print(X)
for i in X:
    # print(rst[i])
    print(rst[i], end=' ')