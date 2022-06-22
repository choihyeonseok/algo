A = list(map(int, input().split()))
B = list(map(int, input().split()))

if A == B:
    print(10, 10)
    print('D')

else :
    result_A = 0
    result_B = 0

    for i in range(10):
        if A[i] > B[i]:
            result_A += 3
            win = 'A'
        elif A[i] < B[i]:
            result_B += 3
            win = 'B'
        else :
            result_A += 1
            result_B += 1
    print(result_A, result_B)

    if result_A == result_B:
        print(win)
    else :
        if result_A > result_B:
            print('A')
        else :
            print('B')