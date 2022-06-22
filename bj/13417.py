import sys
sys.stdin = open("exam_input.txt")

N = int(input())

for _ in range(N):
    n = int(input())
    info = input().split()

    rst = [info[0]]
    for i in range(1, n):
        left = rst[0]
        right = rst[-1]

        if info[i] <= left:
            rst.insert(0, info[i])
        else:
            rst.append(info[i])

    print(''.join(rst))



