import sys
sys.stdin = open("exam_input.txt")

M = int(input())
N = int(input())

rst_sum = 0
rst_min = 10000
for i in range(M, N+1):
    if i != 1:
        for j in range(2, i+1):
            if i % j == 0:
                if j == i:
                    rst_sum += i
                    if rst_min > i:
                        rst_min = i
                break

if rst_sum != 0:
    print(rst_sum)
    print(rst_min)

else:
    print(-1)