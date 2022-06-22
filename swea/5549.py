import sys
sys.stdin = open("test_input1.txt")
input = sys.stdin.readline

check = ['1','3','5','7','9']
T = int(input())
for tc in range(1,T+1):
    info = input()
    if info[-1] in check:
        rst = 'Odd'
    else:
        rst = 'Even'

    print("#{} {}".format(tc, rst))
