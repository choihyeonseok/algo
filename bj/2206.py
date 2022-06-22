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

def bfs(i, j, flag):
    Q = deque()
    Q.append((i, j, flag))

    while Q:
        i, j, flag = Q.popleft()
        if i == N-1 and j == M-1:
            return visited[i][j][flag]

        for _ in range(4):
            ni = di[_] + i
            nj = dj[_] + j

            if 0 <= ni < N and 0 <= nj < M:
                # if info[ni][nj] == 0:
                #     if visited[ni][nj] == 0:
                #         visited[ni][nj] = 1
                #         Q.append((ni,nj,flag))
                # else:
                #     if flag == 0:
                #         flag = 1
                #         if visited[ni][nj] == 0:
                #             visited[ni][nj] = 1
                #             Q.append((ni, nj, flag))
                #     else:
                #         break

                # 다음 이동할 곳이 벽이고, 벽파괴기회를 사용하지 않은 경우
                if info[ni][nj] == 1 and flag == 0:
                    visited[ni][nj][1] = visited[i][j][0] + 1
                    Q.append((ni, nj, 1))
                # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
                elif info[ni][nj] == 0 and visited[ni][nj][flag] == 0:
                    visited[ni][nj][flag] = visited[i][j][flag] + 1
                    Q.append((ni, nj, flag))

    return -1

N, M = map(int, input().split())
info = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
# for i in range(N):
#     for j in range(M):
#         print(info[i][j], end=" ")
#     print()

visited[0][0][0] = 1
print(bfs(0,0,0))

# print("##########################################")
# for i in range(N):
#     for j in range(M):
#         print(visited[i][j], end=" ")
#     print()