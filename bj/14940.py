import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
from itertools import product
# from itertools import combinations_with_replacement

from collections import deque
input = sys.stdin.readline

di = [0,0,-1,1]
dj = [-1,1,0,0]

def bfs(i,j):
    q = deque()
    q.append((i,j,0))
    visited[i][j] = 0

    while q:
        i, j, cnt = q.popleft()
        for _ in range(4):
            ni = di[_] + i
            nj = dj[_] + j

            if 0 <= ni < n and 0 <= nj < m:
                if visited[ni][nj] == 0 and info[ni][nj] == 1:
                    visited[ni][nj] = cnt + 1
                    res[ni][nj] = cnt + 1
                    q.append((ni,nj,cnt+1))


n, m = map(int, input().split())

info = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
res = [[-1]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if info[i][j] == 2:
            bfs(i,j)
            res[i][j] = 0

        if info[i][j] == 0:
            res[i][j] = 0

for i in range(n):
    for j in range(m):
        print(res[i][j], end=" ")
    print()