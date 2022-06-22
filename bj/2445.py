N = int(input())
for i in range(1,2*N):
    if i <= N:
        print('*'*i,end="")
        print(' '*(N-i)*2,end="")
        print('*'*i)
    else:
        print('*'*(2*N-i),end="")
        print(' '*(N-2*N+i)*2,end="")
        print('*'*(2*N-i))
