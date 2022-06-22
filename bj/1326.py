import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

from collections import deque
input = sys.stdin.readline


def bfs(a, b, info, N):
    q = deque()
    q.append(a-1)
    check = [-1]*N
    check[a-1] = 0
    while q:
        node = q.popleft()
        for n in range(node, N, info[node]):
            if check[n] == -1:
                q.append(n)
                check[n] = check[node] + 1
                if n == b-1:
                    return check[n]
        for n in range(node, -1, -info[node]):
            if check[n] == -1:
                q.append(n)
                check[n] = check[node] + 1
                if n == b-1:
                    return check[n]
    return -1

N = int(input())
info = list(map(int, input().split()))
a, b = map(int, input().split())
print(bfs(a, b, info, N))