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

    while q:
        i, j = q.popleft()
        for _ in range(4):
            ni = di[_] + i
            nj = dj[_] + j
            if 0 <= ni < H and 0 <= nj < W:
                if visited[ni][nj] == 0 and info[ni][nj] == '#':
                    visited[ni][nj] = 1
                    q.append((ni,nj))

T = int(input())
for tc in range(1,T+1):
    H, W = map(int, input().split())
    info = [list(map(str, input().rstrip())) for _ in range(H)]
    visited = [[0]*W for _ in range(H)]
    cnt = 0
    # for i in range(H):
    #     for j in range(W):
    #         print(info[i][j], end=" ")
    #     print()

    for i in range(H):
        for j in range(W):
            if info[i][j] == '#' and visited[i][j] == 0:
                bfs(i,j)
                cnt += 1

    print(cnt)

