import sys
sys.stdin = open("exam_input.txt")
input = sys.stdin.readline

n, m = map(int,input().split())
# print(N,K)

up = 1
# up_list = []
down = 1
# down_list = []
for i in range(n,n-m,-1):
    # print(i,N-i+1)
    up *= i
    # up_list.append(i)
    down *= n-i+1
    # down_list.append(N-i+1)

print(up//down)
# print(up_list)
# print(down_list)