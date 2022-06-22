import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

from collections import deque
input = sys.stdin.readline

N = int(input())
visited = [0]*(N+1)

rst = [0]*(N+1)
info = [[] for _ in range(N+1)]
for i in range(N-1):
    S, D = map(int, input().split())
    info[S].append(D)
    info[D].append(S)


def bfs(info, v, visited):
    que = deque([v])
    visited[v] = True
    while que:
        x = que.popleft()
        for i in info[x]:
            if not visited[i]:
                rst[i] = x
                que.append(i)
                visited[i] = True


bfs(info, 1, visited)

for i in range(2, N + 1):
    print(rst[i])
