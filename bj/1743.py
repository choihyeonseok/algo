import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

from collections import deque
input = sys.stdin.readline

di = [-1,1,0,0]
dj = [0,0,-1,1]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    cnt = 1

    while q:
        i,j = q.popleft()
        for _ in range(4):
            ni = di[_] + i
            nj = dj[_] + j
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj] == 0 and info[ni][nj] == 1:
                    visited[ni][nj] = 1
                    q.append((ni,nj))
                    cnt += 1

    return cnt

N, M, K = map(int, input().split())
info = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
for _ in range(K):
    i, j = map(int, input().split())
    info[i-1][j-1] = 1

# for i in range(N):
#     for j in range(M):
#         print(info[i][j], end=" ")
#     print()

max_value = 0
for i in range(N):
    for j in range(M):
        if info[i][j] == 1 and visited[i][j] == 0:
            rst = bfs(i,j)
            if max_value < rst:
                max_value = rst

print(max_value)
