import sys
sys.stdin = open("test_input.txt")

input = sys.stdin.readline

di = [-1,1,0,0]
dj = [0,0,-1,1]

def bfs(i,j,cnt):
    visited[i][j] = 1
    q = []
    q.append((i,j,cnt))

    while q:
        # print(q)
        tmp = q.pop(0)
        tmp_i = tmp[0]
        tmp_j = tmp[1]
        tmp_cnt = tmp[2]

        if tmp_i == N-1 and tmp_j == M-1:
            print(tmp_cnt)
            break

        for _ in range(4):
            ni = di[_] + tmp_i
            nj = dj[_] + tmp_j

            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 1 and visited[ni][nj] == 0:

                    visited[ni][nj] = 1
                    q.append((ni,nj,tmp_cnt+1))








N, M = map(int, input().split())

arr = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
# print(visited)


# for i in range(N):
#     for j in range(M):
#         print(arr[i][j], end=" ")
#     print()

bfs(0,0,1)
