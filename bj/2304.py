import sys
sys.stdin = open("exam_input.txt")
input = sys.stdin.readline


N = int(input())

arr = [[] for _ in range(1001)]
rst = 0

max_value = 0
max_point = 0
last_point = 0

for _ in range(N):
    L, H = map(int,input().split())
    if max_value < H:
        max_value = H
        max_point = L

    arr[L].append(H)
    last_point = max(L, last_point)

# print(max_point)

left = arr[:max_point]
right = arr[max_point:last_point+1]
right.reverse()

tmp = 0
for i in left:
    if len(i) == 0:
        rst += tmp
    else:
        if tmp > i[0]:
            rst += tmp
        else:
            tmp = i[0]
            rst += tmp

tmp = 0
for i in right:
    if len(i) == 0:
        rst += tmp
    else:
        if tmp > i[0]:
            rst += tmp
        else:
            tmp = i[0]
            rst += tmp

print(rst)