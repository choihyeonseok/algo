import sys

sys.stdin = open("test_input.txt")
input = sys.stdin.readline

N = int(input())
check = [[0]*1001 for _ in range(1001)]

for i in range(N):
    x, y, width, height = map(int,input().split())
    for w in range(width):
        for h in range(height):
            check[x+w][y+h] = i+1


# for i in range(1001):
#     for j in range(1001):
#         print(check[i][j], end=" ")
#     print()

for k in range(N):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if check[i][j] == k+1:
                cnt += 1
    
    print(cnt)

