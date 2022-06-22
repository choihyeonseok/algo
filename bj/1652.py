N = int(input())

n = [list(map(str,input())) for _ in range(N)]

count_x = 0
for i in range(N):
    check_x = []
    for j in range(N):
        if n[i][j] == '.':
            check_x.append(n[i][j])
        else :
            if len(check_x) >= 2:
                count_x += 1
                check_x = []
            else:
                check_x = []
    if len(check_x) >= 2:
        count_x += 1

count_y = 0
for i in range(N):
    check_y = []
    for j in range(N):
        if n[j][i] == '.':
            check_y.append(n[j][i])
        else :
            if len(check_y) >= 2:
                count_y += 1
                check_y = []
            else:
                check_y = []
    if len(check_y) >= 2:
        count_y += 1

print(count_x,count_y)