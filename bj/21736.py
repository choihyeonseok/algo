import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

from collections import deque
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    cnt = 0

    while q:
        i, j = q.popleft()
        for _ in range(4):
            ni = di[_] + i
            nj = dj[_] + j

            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj] == 0 and info[ni][nj] != 'X':
                    visited[ni][nj] = 1
                    q.append((ni,nj))
                    if info[ni][nj] == 'P':
                        cnt += 1

    if cnt:
        return cnt
    else:
        return 'TT'


N, M = map(int, input().split())
info = [list(map(str, input().rstrip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]



# for i in range(N):
#     for j in range(M):
#         print(info[i][j], end=" ")
#     print()

flag = 1
for i in range(N):
    for j in range(M):
        if info[i][j] == 'I':
            print(bfs(i,j))
            flag = 0
            break
    if flag == 0:
        break


