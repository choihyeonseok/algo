import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = 10
for tc in range(1,T+1):
    N, info = map(str,input().split())    

    tmp = ['*']
    for i in info:        
        if tmp[-1] == i:
            tmp.pop(-1)
        else:
            tmp.append(i)

    rst = ''
    for i in tmp:
        if i != '*':
            rst += i
        
    print("#{} {}".format(tc,rst))