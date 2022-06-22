A, B = map(str, input().split())
# 세로, 가로
for b in range(len(B)):
    for a in range(len(A)):
        if B[b] == A[a]:
            print(B[b], end='')
        else :
            print('.', end='')
    print()