import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement
input = sys.stdin.readline

N = int(input())
info = list(map(int, input().split()))
print(*sorted(set(info)))