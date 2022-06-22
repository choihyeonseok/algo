import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())

hear = set()
for i in range(N):
    hear.add(input().rstrip())

see = set()
for i in range(M):
    see.add(input().rstrip())

rst = sorted(list(hear & see))

print(len(rst))
for i in rst:
    print(i)