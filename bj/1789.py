import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
input = sys.stdin.readline

S = int(input())

cnt = 0
num = 1
now = 0
while now < S:
    now += num
    cnt += 1
    num += 1

# print(now)
# print(cnt)

if now == S:
    print(cnt)
else:
    print(cnt-1)