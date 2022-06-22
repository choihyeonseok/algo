import sys
sys.stdin = open("test_input.txt")

input = sys.stdin.readline

N = int(input())

cnt = 0
for _ in range(N):
    info = list(map(str, input().rstrip()))
    check = []
    flag = 0
    # print(info)
    for i in info:
        if len(check) == 0:
            check.append(i)

        else:
            if check[-1] != i:
                if i in check:
                    flag = 1
                else:
                    check.append(i)

    if flag == 0:
        cnt += 1

print(cnt)