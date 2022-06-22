import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    info = list(map(str,input().split()))
    rst = []

    if N % 2 == 0:
        left = info[:N//2]
        right = info[N//2:]
        n = N // 2

    else:
        left = info[:N//2+1]
        right = info[N//2+1:]
        right.append('')
        n = N // 2 + 1

    rst.append(left)
    rst.append(right)

    print("#{}".format(tc),end=" ")
    for i in range(n):
        for j in range(2):
            print(rst[j][i],end=" ")
    print()