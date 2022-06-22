import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline

N = int(input())
info = list(map(int, input().split()))

for i in range(N-1,0,-1):
    if info[i-1] > info[i]:
        for j in range(N-1,0,-1):
            if info[i-1] > info[j]:
                info[i-1], info[j] = info[j], info[i-1]
                info = info[:i] + sorted(info[i:],reverse=True)
                print(*info)
                exit()
print(-1)