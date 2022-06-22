import sys
sys.stdin = open("exam_input.txt")

def fac(n):
    if n <= 1:
        return 1
    return n * fac(n-1)

T = int(input())
for _ in range(T):
    R, N = map(int,input().split())
    rst = fac(N) / (fac(R)*fac(N-R))
    print(int(rst))