import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

from collections import deque
input = sys.stdin.readline

di = [0,0,-1,1]
dj = [-1,1,0,0]

def bfs(i,j):
    q = deque()
    # visited[i][j] = 1
    q.append((i,j))
    info[i][j] = 2

    while q:
        i, j = q.popleft()

        for _ in range(4):
            ni = di[_] + i
            nj = dj[_] + j

            if 0 <= ni < M and 0 <= nj < N:
                if info[ni][nj] == 0:
                    q.append((ni,nj))
                    info[ni][nj] = 2
                    if ni == M-1:
                        info[ni][nj] = 2
                        return



M, N = map(int, input().split())
info = [list(map(int, input().rstrip())) for _ in range(M)]

# visited = [[0]*N for _ in range(M)]

for j in range(N):
    # print(info[0][j])
    if info[0][j] == 0:
        bfs(0,j)

# print(info[-1])
if 2 in info[-1]:
    print("YES")

else:
    print("NO")

# for i in range(M):
#     for j in range(N):
#         print(info[i][j], end=" ")
#     print()