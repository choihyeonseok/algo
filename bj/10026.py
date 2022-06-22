import sys
sys.stdin = open("test_input.txt")

input = sys.stdin.readline

di = [-1,1,0,0]
dj = [0,0,-1,1]

def bfs(i,j,cnt):
    q = []
    q.append((i,j,arr[i][j]))
    visited[i][j] = cnt

    while q:
        i, j, info = q.pop(0)

        for _ in range(4):
            ni = di[_] + i
            nj = dj[_] + j

            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0:
                    if arr[ni][nj] == info:
                        visited[ni][nj] = cnt
                        q.append((ni,nj,info))

def bfs2(i,j,cnt):
    q = []
    q.append((i,j,arr[i][j]))
    visited[i][j] = cnt2

    while q:
        i, j, info = q.pop(0)

        for _ in range(4):
            ni = di[_] + i
            nj = dj[_] + j

            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0:
                    if info == 'R' or info == 'G':
                        if arr[ni][nj] == 'R' or arr[ni][nj] == 'G':
                            visited[ni][nj] = cnt2
                            q.append((ni, nj, info))
                    else:
                        if arr[ni][nj] == info:
                            visited[ni][nj] = cnt2
                            q.append((ni,nj,info))

N = int(input())

arr = [list(map(str,input())) for _ in range(N)]

# for i in range(N):
#     for j in range(N):
#         print(arr[i][j], end=" ")
#     print()

cnt = 1
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i,j,cnt)
            cnt += 1

cnt2 = 1
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs2(i,j,cnt2)
            cnt2 += 1

# for i in range(N):
#     for j in range(N):
#         print(visited[i][j], end=" ")
#     print()

print(cnt-1, cnt2-1)