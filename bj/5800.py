import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline

K = int(input())

for k in range(1,K+1):
    info = list(map(int, input().split()))
    rst = info[1:]
    rst.sort()
    gap = 0
    for i in range(info[0]-1):
        if gap < rst[i+1] - rst[i]:
            gap = rst[i+1] - rst[i]
    print("Class {}".format(k))
    print("Max {}, Min {}, Largest gap {}".format(max(rst),min(rst),gap))
