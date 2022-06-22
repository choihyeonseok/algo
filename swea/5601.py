import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    rst = N
    print("#{}".format(tc), end=" ")
    for i in range(N):
        print("1/{}".format(N),end=" ")
    print()
