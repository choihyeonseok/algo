import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

from collections import deque
input = sys.stdin.readline

di = [-2,-2,0,0,2,2]
dj = [-1,1,-2,2,-1,1]

def bfs(r1, c1, r2, c2):
    q = deque()
    visited[r1][c1] = 1
    q.append((r1, c1, 0))

    if r1 == r2 and c1 == c2:
        return 0

    while q:
        i, j, cnt = q.popleft()
        # print(q)
        for _ in range(6):
            ni = di[_] + i
            nj = dj[_] + j

            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    # cnt += 1
                    q.append((ni,nj,cnt+1))

                    if ni == r2 and nj == c2:
                        return cnt+1

    return -1


N = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[0] * N for _ in range(N)]
print(bfs(r1, c1, r2, c2))

# for i in range(l):
#     for j in range(l):
#         print(visited[i][j], end=" ")
#     print()
