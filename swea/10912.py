import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    info = list(map(str,input()))
    info.sort()
    rst = []
    for i in info:
        if len(rst) == 0:
            rst.append(i)
        else:
            if i in rst:
                rst.pop(-1)
            else:
                rst.append(i)

    result = ''
    if len(rst) == 0:
        result = 'Good'
    else:
        for i in rst:
            result += i

    print("#{} {}".format(tc, result))
