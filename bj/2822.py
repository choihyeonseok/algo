import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline

check = []
for t in range(1,9):
    N = int(input())
    # print(N,t)
    check.append((N,t))

check.sort(reverse=True)
# print(check[:5])

rst = 0
rst_list = []
for i in check[:5]:
    rst += i[0]
    rst_list.append(i[1])

print(rst)
# print(rst_list)
rst_list.sort()
print(*rst_list)