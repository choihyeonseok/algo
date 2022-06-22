import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    A = list(map(int, input().split()))
    A.sort()
    print(A[7])