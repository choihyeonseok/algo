import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline

di = [-2,-2,-1,-1,1,1,2,2]
dj = [-1,1,-2,2,-2,2,-1,1]

def bfs(now_i, now_j, next_i, next_j):
    q = []
    visited[now_i][now_j] = 1
    q.append((now_i, now_j, 0))

    if now_i == next_i and now_j == next_j:
        return 0

    while q:
        i, j, cnt = q.pop(0)
        # print(q)
        for _ in range(8):
            ni = di[_] + i
            nj = dj[_] + j

            if 0 <= ni < l and 0 <= nj < l:
                if visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    # cnt += 1
                    q.append((ni,nj,cnt+1))

                    if ni == next_i and nj == next_j:
                        return cnt+1



T = int(input())
for t in range(1,T+1):
    l = int(input())
    now_i, now_j = map(int, input().split())
    next_i, next_j = map(int, input().split())
    visited = [[0] * l for _ in range(l)]
    print(bfs(now_i, now_j, next_i, next_j))

    # for i in range(l):
    #     for j in range(l):
    #         print(visited[i][j], end=" ")
    #     print()
