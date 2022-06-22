import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline

T = int(input())

for t in range(1,T+1):
    info = input().rstrip()
    check = []
    flag = 1
    for i in info:
        if i == '(':
            check.append(i)
        else:
            if check:
                if check[-1] == '(':
                    check.pop(-1)
            else:
                flag = 0
                break

    if check:
        flag = 0
    # print(check)

    if flag == 1:
        print("YES")
    else:
        print("NO")