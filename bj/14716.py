import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

from collections import deque
input = sys.stdin.readline

di = [-1,1,0,0,-1,-1,1,1]
dj = [0,0,-1,1,-1,1,-1,1]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1

    while q:
        i, j = q.popleft()
        for _ in range(8):
            ni = di[_] + i
            nj = dj[_] + j

            if 0 <= ni < M and 0 <= nj < N:
                if visited[ni][nj] == 0 and info[ni][nj] == 1:
                    visited[ni][nj] = 1
                    q.append((ni,nj))

M, N = map(int ,input().split())
info = [list(map(int, input().split())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]

# for i in range(M):
#     for j in range(N):
#         print(info[i][j], end=" ")
#     print()

cnt = 0
for i in range(M):
    for j in range(N):
        if info[i][j] == 1 and visited[i][j] == 0:
            bfs(i,j)
            cnt += 1

print(cnt)
# for i in range(M):
#     for j in range(N):
#         print(visited[i][j], end=" ")
#     print()