import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    info = input()
    rst = 1

    check = info[0]
    for i in range(1,len(info)):
        if info[i] != check:
            check = info[i]
            rst += 1

    if info[0] == '0':
        rst -= 1

    print("#{} {}".format(tc, rst))
