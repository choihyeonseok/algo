import sys
sys.stdin = open("exam_input.txt")


N = int(input())
check = [0] * (N+1)

for i in range(2, N+1):
    check[i] = check[i-1] + 1
    for j in [3,2]:
        if i % j == 0:
            check[i] = min(check[i], check[i // j] + 1)
    # if i % 3 == 0:
    #     check[i] = min(check[i], check[i//3] + 1)
    # if i % 2 == 0:
    #     check[i] = min(check[i], check[i//2] + 1)

print(check[N])