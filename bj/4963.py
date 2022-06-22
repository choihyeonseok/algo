import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

di = [0,0,1,-1,-1,-1,1,1]
dj = [1,-1,0,0,-1,1,1,-1]

def bfs(i,j,cnt):
    q = [(i,j,cnt)]

    while q:
        i, j, cnt = q.pop()
        visited[i][j] = cnt

        for _ in range(8):
            ni = di[_] + i
            nj = dj[_] + j

            if 0 <= ni < h and 0 <= nj < w:
                if info[ni][nj] == 1 and visited[ni][nj] == 0:
                    q.append((ni,nj,cnt))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    info = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]

    cnt = 1
    for i in range(h):
        for j in range(w):
            if info[i][j] == 1 and visited[i][j] == 0:
                bfs(i,j,cnt)
                cnt += 1

    print(cnt-1)
# for i in range(h):
#     for j in range(w):
#         print(info[i][j], end=" ")
#     print()
# print("######################################################")
# for i in range(h):
#     for j in range(w):
#         print(visited[i][j], end=" ")
#     print()