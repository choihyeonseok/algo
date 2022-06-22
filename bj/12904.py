import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline

# S = input().rstrip()
# T = input().rstrip()
#
# q = deque()
# q.append(S)
# rst = 0
# while q:
#     now = q.popleft()
#     if len(now) > len(T):
#         break
#     # print(q)
#     now1 = now + 'A'
#     if now1 == T:
#         rst = 1
#         break
#     now2 = now[::-1] + 'B'
#     if now2 == T:
#         rst = 1
#         break
#
#     q.append(now1)
#     q.append(now2)
#
# print(rst)

S = input().rstrip()
T = input().rstrip()

while (T != S):
    if (len(T) == 0):
        print("0")
        exit()
    if (T[-1] == 'A'):
        T = T[:-1]
    elif (T[-1] == 'B'):
        T = T[::-1]
        T = T[1:]
    else:
        print("0")
        exit()
print("1")