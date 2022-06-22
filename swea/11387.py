import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    D, L, N = map(int,input().split())
    
    rst = 0
    for n in range(N):
        rst += D*(1+n*L/100)

    print("#{} {}".format(tc,int(rst)))