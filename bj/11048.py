import sys
sys.stdin = open("exam_input.txt")
input = sys.stdin.readline

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        # print(arr[i][j])
        if j == 0:
            # print(arr[i][j],(i,j))
            if i != N-1:
                arr[i+1][j] += arr[i][j]

        if i == 0:
            if j != M-1:
                arr[i][j+1] += arr[i][j]

        if i != 0 and j != 0:
            # print((i,j))
            arr[i][j] += max(arr[i-1][j], arr[i][j-1])

print(arr[N-1][M-1])

# for i in range(N):
#     for j in range(M):
#         print(arr[i][j], end=" ")
#     print()