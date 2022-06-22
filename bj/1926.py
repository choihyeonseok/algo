import sys
sys.stdin = open("test_input.txt")
from collections import deque

input = sys.stdin.readline

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def bfs(x, y):
    tmp = 1
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        i, j = queue.popleft()

        for _ in range(4):
            ni = i + di[_]
            nj = j + dj[_]

            if 0 <= ni < n and 0 <= nj < m:
                if info[ni][nj] == 1 and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    queue.append((ni, nj))
                    tmp += 1
    return tmp


n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
info = [list(map(int, input().split())) for _ in range(n)]



cnt, max_value = 0, 0
for i in range(n):
    for j in range(m):
        if info[i][j] == 1 and not visited[i][j]:
            cnt += 1
            max_value = max(max_value, bfs(i, j))

print(cnt)
print(max_value)