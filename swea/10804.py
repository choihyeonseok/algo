
T = int(input())

def change(n):
    if n == 'p':
        return n.replace('p','q') 
    elif n == 'q':
        return n.replace('q','p')
    elif n == 'd':
        return n.replace('d','b')
    elif n == 'b':
        return n.replace('b','d')

for test_case in range(1, T + 1):
    N = input()
    N_reverse = N[::-1]
    result = ''

    for i in range(len(N_reverse)):
        result += change(N_reverse[i])

    print(f'#{test_case} {result}')


