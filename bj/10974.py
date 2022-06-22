import sys
sys.stdin = open("exam_input.txt")

def perm(n, k):
    if k == n:
        print(*p)
    else:
        for i in range(n):
            if used[i] == 0:
                p[k] = arr[i]
                used[i] = 1
                perm(n, k+1)
                used[i] = 0

N = int(input())
arr = list(range(1,N+1))
p = [0] * N
used = [0] * N
perm(N,0)