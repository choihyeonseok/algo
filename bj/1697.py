import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())
q = deque()
maximum = 100000
cnt = [0 for _ in range(100001)]


q.append(n)

while q:
    now = q.popleft()
    if now == k:
        print(cnt[now])
        break

    for next in (now*2,now+1,now-1):
        if 0 <= next <= maximum and not cnt[next]:
            cnt[next] = cnt[now] + 1
            q.append(next)