import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
info = [[1]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        info[i][j] = info[i-1][j] + info[i][j-1]

if info[N][M] < K:
    print(-1)
else:
    rst = ''
    while True:
        if N == 0 or M == 0:
            rst += 'a'*N + 'z'*M
            # rst +=
            break

        flag = info[N-1][M]
        if K <= flag:
            rst += 'a'
            N -= 1
        else:
            rst += 'z'
            M -= 1
            K -= flag
    print(rst)
