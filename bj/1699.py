import sys
sys.stdin = open("exam_input.txt")
input = sys.stdin.readline

N = int(input())
cnt = 4

def sol(n, count):
    global cnt

    if n == 0:
        cnt = min(cnt, count)
        return
    if count > cnt:
        return
    for i in range(int(n**0.5), int((n // (4-count))**0.5), -1):
        sol(n - i ** 2, count + 1)

sol(N, 0)
print(cnt)