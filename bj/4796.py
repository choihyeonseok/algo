import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
input = sys.stdin.readline

n = 0
while True:
    L, P, V = map(int, input().split())
    n += 1
    if L == 0 and P == 0 and V == 0:
        break

    rst = 0
    while V > P:
        V -= P
        rst += L

    if V > L:
        rst += L
    else:
        rst += V

    print("Case {}: {}".format(n,rst))

