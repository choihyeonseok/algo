import sys
sys.stdin = open("exam_input.txt")

E, S, M = map(int, input().split())

# print(E, S, M)

N = 1
while True:
    a, b, c = N % 15, N % 28, N % 19

    if a == 0:
        a = 15
    if b == 0:
        b = 28
    if c == 0:
        c = 19

    if (a, b, c) == (E, S, M):
        print(N)
        break

    N += 1