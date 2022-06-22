T = int(input())

for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    result_sum = 0
    for i in range(len(a)):
        if a[i] % 2 == 1:
            result_sum += a[i]
    print(f'#{test_case} {result_sum}')