import sys
sys.stdin = open("exam_input.txt")
input = sys.stdin.readline

N, K = map(int,input().split())
# print(N,K)

up = 1
# up_list = []
down = 1
# down_list = []
for i in range(N,N-K,-1):
    # print(i,N-i+1)
    up *= i
    # up_list.append(i)
    down *= N-i+1
    # down_list.append(N-i+1)

print(up//down % 10007)
# print(up_list)
# print(down_list)