import sys
sys.stdin = open("test_input.txt")

input = sys.stdin.readline

N = int(input())
num = []
for _ in range(N):
    n = int(input())
    num.append(n)
num.sort()
for i in num:
    print(i)