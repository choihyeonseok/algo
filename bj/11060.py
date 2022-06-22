import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

from collections import deque
input = sys.stdin.readline

def bfs(now, value, cnt):
    q = deque()
    q.append((now, value, cnt))
    visited[now] = 1

    while q:
        now, value, cnt = q.popleft()
        for next in range(1, value+1):
            if now + next < N and visited[now+next] == 0:
                visited[now+next] = 1
                q.append((now+next, A[now+next], cnt+1))
                if now+next == N-1:
                    return cnt+1
    return -1


N = int(input())
A = list(map(int, input().split()))
if N == 1:
    print(0)
else:
    visited = [0]*N
    print(bfs(0, A[0], 0))
# print(A)