import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    info = list(map(str,input()))
    H = int(input())
    point = list(map(int, input().split()))
    point.sort(reverse=True)

    for i in point:
        info.insert(i,'-')
    rst = ''
    for i in info:
        rst += i

    print("#{} {}".format(tc, rst))
