import sys
sys.stdin = open("exam_input.txt")
input = sys.stdin.readline


A, B = map(int,input().split())
rst = 1
# rst_list = []
# print(A,B)

if A > B:
    A, B = B, A

if B % A == 0:
    print(A)
    rst = B

else:
    tmp = 2
    while A != 1:
        if tmp == B:
            break

        if A % tmp == 0 and B % tmp == 0:
            A //= tmp
            B //= tmp
            rst *= tmp
            tmp = 1
            # rst_list.append(tmp)
        tmp += 1
    print(rst)
    rst *= A * B

print(rst)




