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

    cnt_v = 0
    cnt_k = 0

    if info[i][j] == 'v':
        cnt_v += 1
    if info[i][j] == 'k':
        cnt_k += 1

    while q:
        i, j = q.popleft()
        for _ in range(4):
            ni = di[_] + i
            nj = dj[_] + j

            if 0 <= ni < R and 0 <= nj < C:
                if visited[ni][nj] == 0 and info[ni][nj] != '#':
                    if info[ni][nj] == 'v':
                        cnt_v += 1
                    if info[ni][nj] == 'k':
                        cnt_k += 1

                    visited[ni][nj] = 1
                    q.append((ni,nj))

    # print(cnt_k, cnt_v)
    if cnt_k > cnt_v:
        cnt_v = 0
    else:
        cnt_k = 0

    return cnt_k, cnt_v



R, C = map(int, input().split())
info = [list(map(str, input().rstrip())) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
# for i in range(R):
    # for j in range(C):
    #     print(info[i][j], end=" ")
    # print()

k = 0
v = 0
for i in range(R):
    for j in range(C):
        if info[i][j] != '#' and visited[i][j] == 0:
            rst = bfs(i,j)
            # print((i,j))
            k += rst[0]
            v += rst[1]

print(k,v)