import sys
sys.stdin = open("exam_input.txt")

N = int(input())

check = []
for _ in range(N):
    x, y = map(int, input().split())
    check.append((x, y))

rst = []
for i in range(N):
    cnt = 1
    for j in range(N):
        if check[i][0] < check[j][0] and check[i][1] < check[j][1]:
            cnt += 1
    rst.append(cnt)

print(*rst)