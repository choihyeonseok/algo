import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    P, Q, R, S, W = map(int,input().split())
    A = P * W
    
    if W <= R:
        B = Q
    else:
        B = Q + S * (W-R)
    
    rst = min(A,B)
    print("#{} {}".format(tc,rst))