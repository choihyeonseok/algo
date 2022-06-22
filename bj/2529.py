import sys
sys.stdin = open("test_input.txt")
from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline

k_list = ["0","1","2","3","4","5","6","7","8","9"]
k_list2 = ["9","8","7","6","5","4","3","2","1","0"]
k = int(input())
info = list(map(str, input().split()))
# print(info)

for i in permutations(k_list2, k+1):
    # print(i)
    flag = 1
    for j in range(k):
        if info[j] == '<':
            if i[j] > i[j+1]:
                flag = 0
                break
        else:
            if i[j] < i[j+1]:
                flag = 0
                break

    if flag == 1:
        print("".join(i))
        break

for i in permutations(k_list, k+1):
    # print(i)
    flag = 1
    for j in range(k):
        if info[j] == '<':
            if i[j] > i[j+1]:
                flag = 0
                break
        else:
            if i[j] < i[j+1]:
                flag = 0
                break

    if flag == 1:
        print("".join(i))
        break

