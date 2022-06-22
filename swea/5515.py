import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

day = [0,4,0,1,4,6,2,4,0,3,5,1,3]

T = int(input())
for tc in range(1,T+1):
    m, d = map(int,input().split())
    check = day[m]
    rst = (check + (d - 1) % 7) % 7
    print("#{} {}".format(tc, rst))
