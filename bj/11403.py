import sys
sys.stdin = open("test_input.txt")

input = sys.stdin.readline

def bfs(info):
    q = []
    check = []
    visited = [[0] * N for tmp in range(N)]
    for i in range(N):
        if info[i] == 1:
            adj[_][i] = 1
            visited[_][i] = 1
            q.append((_,i))
            check.append(i)

    while q:
        # print(q)
        r, c = q.pop(0)
        for ii in range(N):
            if arr[c][ii] == 1:
                if visited[c][ii] == 0:
                    adj[c][ii] = 1
                    visited[c][ii] = 1
                    q.append((c,ii))
                    check.append(ii)

    for tmp in check:
        adj[_][tmp] = 1
    # print(check, '체크', _)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
adj = [[0] * N for _ in range(N)]

for _ in range(N):
    bfs(arr[_])

for i in range(N):
    for j in range(N):
        print(adj[i][j], end=" ")
    print()
