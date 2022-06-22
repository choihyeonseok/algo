import sys
sys.stdin = open("test_input.txt")

input = sys.stdin.readline

def bfs(info):
    global rst
    q = []
    for r in range(n+1):
        if info[r] == 1:
            q.append((r,cnt+1))
            visited[r] = 1

    while q:
        # print(q)
        tmp_r, tmp_cnt = q.pop(0)
        # if tmp_cnt == n:
        #     print(-1)
        #     break
        tmp_info = arr[tmp_r]
        for r in range(n+1):
            if tmp_info[r] == 1 and visited[r] == 0:
                q.append((r, tmp_cnt+1))
                visited[r] = 1
                if r == p2:
                    rst = tmp_cnt+1
                    print(rst)
                    quit()
                # if tmp_cnt+1 == n:
                #     print(-1)
                #     quit()
                # if len(q) == 1:
                #     print(-1)
                #     quit()


n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
arr = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1

# for i in range(n+1):
#     for j in range(n+1):
#         if i != 0 and j != 0:
#             print(arr[i][j], end=" ")
#     print()

cnt = 0
rst = 0
bfs(arr[p1])
if rst == 0:
    print(-1)