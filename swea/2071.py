T = int(input())

for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    result_sum = 0
    for i in range(len(a)):
        result_sum += a[i]
    print(f'#{test_case} {round(result_sum / len(a))}')
    