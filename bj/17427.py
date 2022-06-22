import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
input = sys.stdin.readline

N = int(input())

rst = [i * (N//i) for i in range(1,N+1)]
print(sum(rst))