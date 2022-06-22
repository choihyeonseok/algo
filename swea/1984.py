import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())

for tc in range(1,T+1):
    case = list(map(int,input().split()))
    max = 0
    min = 10000
    for i in case:
        if max < i:
            max = i        
        if min > i:
            min = i
    cnt = 0
    for i in case:
        cnt += i
    cnt -= max + min
    print("#{} {}".format(tc,int(cnt/8+0.5)))