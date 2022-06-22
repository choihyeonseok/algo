T = int(input())
for test_case in range(1, T + 1):
    N, A, B = map(int, input().split())
    if A > B:        
        result_max = B
    else :        
        result_max = A

    result_min = (A + B) - N

    if result_min < 0:
        result_min = 0

    print(f'#{test_case} {result_max} {result_min}')