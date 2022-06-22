import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
check = [0]*(N+1)
for _ in range(M):
    u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    arr[u][v] = 1
    check[u] = check[v] = 1
tmp = []
for i in range(1,N+1):
    for j in range(1, N+1):
        if arr[i][j] == 1:
            if len(tmp) == 0:
                tmp.append([i,j])
            if i in tmp[-1] or j in tmp[-1]:
                if i not in tmp[-1]:
                    tmp[-1].append(i)
                if j not in tmp[-1]:
                    tmp[-1].append(j)
            else:
                tmp.append([i,j])
cnt = 0
for i in range(1,N+1):
    if check[i] == 0:
        cnt += 1
print(len(tmp)+cnt)