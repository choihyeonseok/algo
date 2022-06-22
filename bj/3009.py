T = 3
result_x = []
result_y = []
for test_case in range(1, T + 1):
    x, y = map(int, input().split())
    result_x.append(x)
    result_y.append(y)

for i in result_x:
    if result_x.count(i) == 1:
        X = i

for j in result_y:
    if result_y.count(j) == 1:
        Y = j

print(f'{X} {Y}')
