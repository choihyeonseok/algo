import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

from collections import deque
input = sys.stdin.readline

import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

from collections import deque
input = sys.stdin.readline

def bfs(i,j,value):
    q = deque()
    if i + value < N:
        q.append((i+value,j,info[i+value][j]))
        visited[i+value][j] = 1
    if j + value < N:
        q.append((i,j+value,info[i][j+value]))
        visited[i][j+value] = 1

    while q:
        i, j, value = q.popleft()
        if i + value < N and visited[i+value][j] == 0:
            if info[i+value][j] == -1:
                return "HaruHaru"
            q.append((i+value, j, info[i+value][j]))
            visited[i+value][j] = 1

        if j + value < N and visited[i][j+value] == 0:
            if info[i][j+value] == -1:
                return "HaruHaru"
            q.append((i, j+value, info[i][j+value]))
            visited[i][j+value] = 1

    return "Hing"




N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         print(info[i][j], end=" ")
#     print()

print(bfs(0,0,info[0][0])) 