import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

from collections import deque
input = sys.stdin.readline

def bfs(s,t):
    q = deque()
    q.append((s,''))
    visited.append(s)

    if s == t:
        return 0

    while q:
        # print(q)
        s, process = q.popleft()

        ns = s
        for next in [(ns*ns, '*'), (ns+ns, '+'), (ns-ns, '-'), (ns//ns, '/')]:
            if 0 < next[0] < t+1:
                if next[0] not in visited:
                    visited.append(next[0])
                    q.append((next[0], process + next[1]))

                    if next[0] == t:
                        return process + next[1]



    return -1


s, t = map(int, input().split())
visited = []
print(bfs(s,t))
