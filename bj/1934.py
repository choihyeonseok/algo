import sys
sys.stdin = open("exam_input.txt")
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int,input().split())
    rst = 1
    if A > B:
        A, B = B, A
    if B % A == 0:
        rst = B
    else:
        tmp = 2
        while A != 1:
            if tmp == B:
                break
            if A % tmp == 0 and B % tmp == 0:
                A //= tmp
                B //= tmp
                rst *= tmp
                tmp = 1
            tmp += 1
        rst *= A * B
    print(rst)