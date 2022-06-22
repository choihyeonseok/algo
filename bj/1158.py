import sys
sys.stdin = open("test_input.txt")
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr = deque(list(range(1, N+1)))

print("<",end="")
while arr:
    for i in range(K-1):
        arr.append(arr[0])
        arr.popleft()

    print(arr.popleft(), end="")
    if arr:
        print(",", end=" ")
print(">")