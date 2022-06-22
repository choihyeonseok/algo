import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    check = []
    result = 0
    n = 0

    while len(check) != 10:
        result += 1
        n = result * N
        while n > 0:
            if (n % 10) not in check:
                check.append(n % 10)
            n //= 10

    print("#{} {}".format(tc,result*N))