import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline

def bfs(num):
    q = []
    q.append((num-1, A[num-1]))
    visited[num-1] = 1

    while q:
        num, value = q.pop(0)
        for next in [num-value, num+value]:
            if 0 <= next < n:
                if visited[next] == 0:
                    visited[next] = 1
                    q.append((next, A[next]))

n = int(input())
visited = [0]*n
A = list(map(int, input().split()))
S = int(input())

bfs(S)
print(sum(visited))