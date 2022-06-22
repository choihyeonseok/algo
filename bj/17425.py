import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
input = sys.stdin.readline

F = [1] * 1000001
G = [0] * 1000001

for i in range(2, 1000001):
    for j in range(i, 1000001, i):
        F[j] += i

for i in range(1, 1000001):
    G[i] = G[i-1] + F[i]

# ans = []

T = int(input())
for _ in range(T):
    # ans.append(G[int(input())])
    print(G[int(input())])

# print('\n'.join(map(str, ans)) + "\n")