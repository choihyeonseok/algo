import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

from collections import deque
input = sys.stdin.readline

def bfs(A,B,N,M):
    q = deque()
    q.append((N,0))
    visited[N] = 1
    if N == M:
        return 0

    while q:
        now, cnt = q.popleft()
        for next in [now-1,now+1,now-A,now+A,now-B,now+B,now*A,now*B]:
            if 0 <= next < 100001:
                if visited[next] == 0:
                    visited[next] = 1
                    q.append((next,cnt+1))
                    if next == M:
                        return cnt+1

A, B, N, M = map(int, input().split())
visited = [0] * 100001
print(bfs(A,B,N,M))