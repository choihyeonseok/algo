import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())

for tc in range(1,T+1):
    A, B = map(int,input().split())
    arr_A = list(map(int,input().split()))
    arr_B = list(map(int,input().split()))

    if A < B:
        max = 0
        for i in range(B-A+1):
            check = []
            for j in range(A):
                check.append(arr_B[i+j])
            rst = 0
            for k in range(A):
                for l in range(A):
                    if k == l:
                        rst += check[k] * arr_A[l]
            if max < rst:
                max = rst
        print("#{} {}".format(tc,max))

    else:
        max = 0
        for i in range(A-B+1):
            check = []
            for j in range(B):
                check.append(arr_A[i+j])
            rst = 0
            for k in range(B):
                for l in range(B):
                    if k == l:
                        rst += check[k] * arr_B[l]
            if max < rst:
                max = rst
                
        print("#{} {}".format(tc,max))