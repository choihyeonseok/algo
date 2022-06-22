import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

from collections import deque
input = sys.stdin.readline

def bfs(F, S, G, U, D):
    q = deque()
    q.append((S,0))
    visited[S] = 1

    if S == G:
        return 0

    while q:
        now, cnt = q.popleft()

        for change in [U, D*(-1)]:
            next = now + change

            if 0 < next <= F:
                if visited[next] == 0:
                    visited[next] = 1
                    q.append((next, cnt+1))
                    if next == G:
                        return cnt + 1

    return "use the stairs"





F, S, G, U, D = map(int, input().split())
visited = [0] * (F+1)
print(bfs(F, S, G, U, D))