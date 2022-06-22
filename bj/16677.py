import sys
sys.stdin = open("exam_input.txt")

m = input()
N = int(input())

tmp = []
max_value = 0

for _ in range(N):
    w, g = input().split()
    if len(m) < len(w):
        num = int(g) / (len(w) - len(m))
        if max_value <= num:
            max_value = num
            tmp.append((w, num))

check = []
for i in tmp:
    if i[1] == max_value:
        check.append(i)

rst = ''
for i in check:
    if rst < i[0]:
        rst = i[0]

flag = 0
check_num = []
for i in range(len(m)):
    for j in range(i,len(rst)):
        if flag == 0:
            if m[i] == rst[j]:
                check_num.append(i)
                break
            else:
                flag = -1
        else:
            rst = 'No Jam'
            break

origin_num = check_num
check_num.sort()

if origin_num != check_num:
    rst = 'No Jam'

print(rst)