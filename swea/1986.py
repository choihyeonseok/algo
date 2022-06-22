T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    N_list = [1,2,3,4,5,6,7,8,9,10]
    result = 0
    for i in range(0, N):
        if i % 2 != 0:
            N_list[i] = N_list[i] * (-1)
        result += N_list[i]
    print(f'#{test_case} {result}')