# 소수의 타입은 float

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    count_a, count_b, count_c, count_d, count_e = 0, 0, 0, 0, 0
    num_list = [2, 3, 5, 7, 11]

    for num in num_list:
        while N % num == 0:
            N = N/num
            if num == 2:
                count_a += 1
            if num == 3:
                count_b += 1
            if num == 5:
                count_c += 1
            if num == 7:
                count_d += 1
            if num == 11:
                count_e += 1

    print(f'#{test_case} {count_a} {count_b} {count_c} {count_d} {count_e}')
