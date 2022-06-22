import sys
sys.stdin = open("test_input.txt")

input = sys.stdin.readline

di = [-1,1,0,0]
dj = [0,0,-1,1]

def bfs(r,c):
    visited[r][c] = 1
    q = []
    tmp = []
    q.append((r,c))
    tmp.append((r,c))

    while q:
        # print(q)
        tmp_r, tmp_c= q.pop(0)
        for _ in range(4):
            ni = di[_] + tmp_r
            nj = dj[_] + tmp_c

            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0 and arr[ni][nj] == 1:
                    visited[ni][nj] = 1
                    q.append((ni,nj))
                    tmp.append((ni,nj))

    rst.append(len(tmp))

N = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

# for i in range(N):
#     for j in range(N):
#         print(arr[i][j], end=" ")
#     print()

rst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            bfs(i,j)

print(len(rst))
rst.sort()
# print(rst)
for i in rst:
    print(i)
