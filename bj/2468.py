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

def bfs(i,j,h):
    q = deque()
    q.append((i,j,h))
    visited[i][j] = 1

    while q:
        i,j,h = q.popleft()
        # print(q)
        for _ in range(4):
            ni = di[_] + i
            nj = dj[_] + j

            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0 and info[ni][nj] > h:
                    visited[ni][nj] = 1
                    q.append((ni,nj,h))



N = int(input())

info = [list(map(int, input().split())) for _ in range(N)]

# for i in range(N):
#     for j in range(N):
#         print(info[i][j], end=" ")
#     print()

h = 1
max_value = 0
while True:
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if info[i][j] > h and visited[i][j] == 0:
                cnt += 1
                bfs(i,j,h)

    # print(cnt)
    if max_value < cnt:
        max_value = cnt

    h += 1

    if cnt == 0:
        break


print(max_value)