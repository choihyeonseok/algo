import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    money = [50000,10000,5000,1000,500,100,50,10]
    check = [0,0,0,0,0,0,0,0]
    
    for i in range(8):
        if N >= money[i]:
            while N - money[i]>= 0:
                N = N - money[i]
                check[i] += 1

    print("#{}".format(tc))
    print(*check)