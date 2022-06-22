import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

from collections import deque
input = sys.stdin.readline

# di = [0,1]
# dj = [1,0]

N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
di = [[0, 1], [1, 0]]
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 0
q = deque()
q.append((0, 0))

while q:
    y, x = q.popleft()
    for _ in range(2):
        next_y, next_x = y, x
        for j in range(info[y][x]):
            next_y, next_x = next_y + di[_][0], next_x + di[_][1]
            if 0 <= next_y < N and 0 <= next_x < M and visited[next_y][next_x] == 0:
                q.append((next_y, next_x))
                visited[next_y][next_x] = visited[y][x] + 1


print(visited[-1][-1])