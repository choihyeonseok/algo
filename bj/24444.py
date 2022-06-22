import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
from itertools import product
# from itertools import combinations_with_replacement

from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())

# graph
check = [[] for _ in range(N + 1)]

# 입력받는 간선 정보 그래프화
for i in range(M):
    u, v = map(int, input().split())
    check[u].append(v)
    check[v].append(u)

# 정렬
for i in range(N + 1):
    check[i].sort()


# BFS 함수
def bfs(check):
    global R
    visited = [0]*(N+1)
    q = deque([R])
    visited[R] = 1
    cnt = 2

    while q:
        R = q.popleft()

        for i in check[R]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = cnt
                cnt += 1  # n+1 번째 방문 정점

    for i in visited[1::]:
        print(i)

# 정점 리스트


bfs(check)

# 출력


# print(check)