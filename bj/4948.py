import sys

sys.stdin = open("exam_input.txt")

input = sys.stdin.readline

def prime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

while True:
    M = int(input())
    if M == 0:
        break

    cnt = 0
    for i in range(M+1, 2*M+1):
        if prime(i):
            cnt += 1

    print(cnt)
