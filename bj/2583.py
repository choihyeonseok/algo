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
    q.append((i,j,1))
    visited[i][j] = 1
    check = 0

    while q:
        i, j, cnt = q.popleft()
        check += 1
        # print(q)

        for _ in range(4):
            ni = di[_] + i
            nj = dj[_] + j

            if 0 <= ni < M and 0 <= nj < N:
                if visited[ni][nj] == 0:
                    if info[ni][nj] == 0:
                        visited[ni][nj] = cnt
                        q.append((ni,nj,cnt))

    return check

M, N, K = map(int, input().split())
info = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            # print(x,y)
            info[y][x] = 1

# for i in range(M):
#     for j in range(N):
#         print(info[i][j], end=" ")
#     print()
#
# print("################################")
rst = 0
rst_list = []
for i in range(M):
    for j in range(N):
        if info[i][j] == 0 and visited[i][j] == 0:
            rst += 1
            rst_list.append(bfs(i,j))
rst_list.sort()
print(rst)
print(*rst_list)

# for i in range(M):
#     for j in range(N):
#         print(visited[i][j], end=" ")
#     print()