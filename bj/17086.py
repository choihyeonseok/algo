import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]

di = [0,0,-1,1,1,1,-1,-1]
dj = [-1,1,0,0,-1,1,-1,1]

def bfs(q):
    while q:
        i, j, cnt = q.popleft()
        for _ in range(8):
            ni = di[_] + i
            nj = dj[_] + j

            if 0 <= ni < N and 0 <= nj < M:
                if info[ni][nj] == 0:
                    info[ni][nj] = cnt + 1
                    q.append((ni,nj,cnt+1))

    return cnt

q = deque()
for i in range(N):
    for j in range(M):
        if info[i][j] == 1:
            q.append((i,j,0))

print(bfs(q))

# for i in range(N):
#     for j in range(M):
#         print(info[i][j], end=" ")
#     print()