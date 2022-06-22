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

def bfs(a, b):
    q = deque()
    q.append((a, b))
    while q:
        i, j = q.popleft()
        visited[i][j] = True
        for _ in range(4):
            ni = i + di[_]
            nj = j + dj[_]
            if 0 <= ni < n and 0 <= nj < m:
                if info[ni][nj] != 0 and visited[ni][nj] == False:
                    visited[ni][nj] = True
                    q.append((ni, nj))
                elif info[ni][nj] == 0:
                    cnt[i][j] += 1
    return 1


n, m = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]

day = 0
check = False

while True:
    visited = [[False] * m for _ in range(n)]
    cnt = [[0] * m for _ in range(n)]
    rst = []
    for i in range(n):
        for j in range(m):
            if info[i][j] != 0 and visited[i][j] == False:
                rst.append(bfs(i, j))

    for i in range(n):
        for j in range(m):
            info[i][j] -= cnt[i][j]
            if info[i][j] < 0:
                info[i][j] = 0

    if len(rst) == 0:
        break
    if len(rst) >= 2:
        check = True
        break
    day += 1

if check:
    print(day)
else:
    print(0)


