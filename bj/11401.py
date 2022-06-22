import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

N, K = map(int, input().split())
check = 1000000007

def fact(N):
    n = 1
    for i in range(2, N + 1):
        n = (n * i) % check
    return n

def double(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n

    tmp = double(n, k // 2)
    if k % 2:
        return tmp * tmp * n % check
    else:
        return tmp * tmp % check

up = fact(N)
down = fact(N - K) * fact(K) % check

# 페르마의 소정리 이용해서 조합 공식 곱셈 형태로 변형
print(up * double(down, check - 2) % check)