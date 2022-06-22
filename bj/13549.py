import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline

def bfs(N, K):
    q = []
    q.append((N, 0))
    visited[N] = 1

    if N == K:
        return 0

    while q:
        # print(q)
        now, cnt = q.pop(0)
        for next in [(now*2, 0), (now-1, 1), (now+1, 1)]:
            if 0 <= next[0] < 200001 and visited[next[0]] == 0:
                visited[next[0]] = 1
                q.append((next[0], cnt+next[1]))

                if next[0] == K:
                    return cnt+next[1]

    # return


N, K = map(int, input().split())
visited = [0] * 200001

print(bfs(N, K))
