import sys

sys.stdin = open("test_input.txt")
input = sys.stdin.readline

N = int(input())
check = []
for i in range(N):
    x,y = map(int,input().split())
    # print(x,y)
    check.append([x,y])

# print(check)

max_value_x = -2000
min_value_x = 2000
max_value_y = -2000
min_value_y = 2000

for i in check:
    if i[0] > max_value_x:
        max_value_x = i[0]

    if i[0] < min_value_x:
        min_value_x = i[0]
    
    if i[1] > max_value_y:
        max_value_y = i[1]

    if i[1] < min_value_y:
        min_value_y = i[1]

# print(max_value_x, max_value_y)
# print(min_value_x, min_value_y)

len_x = max_value_x - min_value_x
len_y = max_value_y - min_value_y
print(len_x,len_y)
result = max(len_x,len_y)

print(check)
cnt = 0
for i in check:
    if i[0] != min_value_x + max(len_x,len_y) and i[0] != min_value_x:
        if i[1] != min_value_y + max(len_x,len_y) and i[1] != min_value_y:
            print(i[0],i[1])
            cnt += 1
            result = -1

print(cnt)
print(result)

