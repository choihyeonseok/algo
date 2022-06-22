import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

N = int(input())
                
color = [list(map(str,input())) for _ in range(N)]


for i in range(N):
    for j in range(N):
        print(color[i][j], end=" ")
    print()

