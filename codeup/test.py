import sys
sys.stdin = open("test.txt")

N = int(input())
A, B = map(int,input().split())
C = int(input())

for _ in range(N):
    D = int(input())