T = int(input())
for test_case in range(1, T + 1):
    N1, N2 = map(int, input().split())
    result = ''
    if N1 < N2:
        result = '<'
    elif N1 == N2:
        result = '='
    else :
        result = '>'
    print(f'#{test_case} {result}')