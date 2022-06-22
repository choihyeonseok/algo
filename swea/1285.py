import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    case = list(map(int,input().split()))
    min = 100000
    for i in case:
        check = abs(i)
        if check < min:
            min = check

    cnt = 0
    for i in case:
        if abs(i) == min:
            cnt += 1
            
    print("#{} {} {}".format(tc,min,cnt))