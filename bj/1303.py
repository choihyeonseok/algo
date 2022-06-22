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

def bfs(i,j,color):
    q = deque()
    q.append((i, j, color))
    visited[i][j] = 1
    cnt = 1

    while q:
        i, j, color = q.popleft()
        # print(q)
        for _ in range(4):
            ni = di[_] + i
            nj = dj[_] + j

            if 0 <= ni < M and 0 <= nj < N:
                if visited[ni][nj] == 0 and info[ni][nj] == color:
                    visited[ni][nj] = 1
                    cnt += 1
                    q.append((ni,nj,color))

    # print(cnt, color)
    return cnt, color

N, M = map(int, input().split())
info = [list(map(str, input().rstrip())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
# for i in range(M):
#     for j in range(N):
#         print(info[i][j], end=" ")
#     print()

cnt_W = 0
cnt_B = 0
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            rst = bfs(i,j,info[i][j])
            if rst[1] == 'W':
                cnt_W += rst[0] * rst[0]
            else:
                cnt_B += rst[0] * rst[0]

# print("##################################")
# for i in range(M):
#     for j in range(N):
#         print(visited[i][j], end=" ")
#     print()

print(cnt_W, cnt_B)