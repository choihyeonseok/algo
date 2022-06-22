import sys
sys.stdin = open("test_input.txt")

N, M = map(int,input().split())
arr = [input() for _ in range(N)]

cnt = 0
for i in range(N):
    check = []
    for j in range(M):
        if arr[i][j] == '-':
            if len(check) == 0:
                cnt += 1
                check.append(arr[i][j])
        else :
            check = []

for j in range(M):
    check = []
    for i in range(N):
        if arr[i][j] == '|':
            if len(check) == 0:
                cnt += 1
                check.append(arr[i][j])
        else :
            check = []

print(cnt)