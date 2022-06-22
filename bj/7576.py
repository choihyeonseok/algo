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

def bfs(q):
    while q:
        i, j = q.popleft()
        for _ in range(4):
            ni = di[_] + i
            nj = dj[_] + j
            if 0 <= ni < N and 0 <= nj < M:
                if info[ni][nj] == 0:
                    info[ni][nj] = info[i][j] + 1
                    q.append([ni,nj])



M, N = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
rst = 0
check = deque([])
for i in range(N):
    for j in range(M):
        if info[i][j] == 1:
            check.append([i,j])

# print(check)
bfs(check)
for i in info:
    for j in i:
        if j == 0:
            print(-1)
            exit()

    rst = max((rst, max(i)))
print(rst-1)