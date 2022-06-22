import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

N = [1,4,9,121,484]

T = int(input())
for tc in range(1,T+1):
    A, B = map(int,input().split())    

    rst = 0
    for i in N:
        if A <= i <= B:
            rst += 1

    
    print("#{} {}".format(tc,rst))