import sys
sys.stdin = open("exam_input.txt")


N = int(input())
n = list(map(int,input().split()))

for i in range(N):
    if n[i] > 0:
        print(n[i])