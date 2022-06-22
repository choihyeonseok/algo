import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    # print(v, end=" ")
    rst1.append(v)

    for w in range(1, N+1):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)

def bfs(v):
    q = []
    visited = [0] * (N+1)
    q.append(v)
    visited[v] = 1
    while q:
        t = q.pop(0)
        # print(t)
        rst2.append(t)
        for i in range(1, N+1):
            if adj[t][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1

N, M, V = map(int, input().split())

adj = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

rst1 = []
rst2 = []

for _ in range(M):
    start, end = map(int, input().split())
    adj[start][end] = 1
    adj[end][start] = 1

dfs(V)
bfs(V)

print(*rst1)
print(*rst2)