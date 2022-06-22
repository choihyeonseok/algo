import sys
N = int(sys.stdin.readline())
result = 0

for i in range(N):
    result += int(sys.stdin.readline())

print(result - N + 1)