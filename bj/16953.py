import sys
sys.stdin = open("exam_input.txt")

A, B = map(int,input().split())

cnt = 1
while True:
    if B % 10 == 1:
        B = B // 10
        cnt += 1

    else:
        B = B / 2
        cnt += 1

    if B == A:
        print(cnt)
        break

    if B < A:
        print(-1)
        break