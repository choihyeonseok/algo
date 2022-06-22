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
    cnt_o = 0
    cnt_v = 0
    q.append((i,j))
    visited[i][j] = 1
    if info[i][j] == 'v':
        cnt_v += 1
    if info[i][j] == 'o':
        cnt_o += 1

    while q:
        i, j = q.popleft()
        # print(q)
        for _ in range(4):
            ni = di[_] + i
            nj = dj[_] + j

            if 0 <= ni < R and 0 <= nj < C:
                if visited[ni][nj] == 0 and info[ni][nj] != '#':
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                    if info[ni][nj] == 'v':
                        cnt_v += 1
                    if info[ni][nj] == 'o':
                        cnt_o += 1

    # print(cnt_o, cnt_v)

    if cnt_o > cnt_v:
        cnt_v = 0
    else:
        cnt_o = 0

    return cnt_o, cnt_v


R, C = map(int, input().split())
info = [list(map(str, input().rstrip())) for _ in range(R)]
visited = [[0]*C for _ in range(R)]

# for i in range(R):
#     for j in range(C):
#         print(info[i][j], end=" ")
#     print()

rst_o = 0
rst_v = 0
for i in range(R):
    for j in range(C):
        if info[i][j] != '#' and visited[i][j] == 0:
            rst = bfs(i,j)
            # print(rst)
            rst_o += rst[0]
            rst_v += rst[1]

# for i in range(R):
#     for j in range(C):
#         print(visited[i][j], end=" ")
#     print()

print(rst_o, rst_v)