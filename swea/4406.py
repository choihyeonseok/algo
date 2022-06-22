import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

check = ['a','e','i','o','u']

T = int(input())
for tc in range(1,T+1):
    info = input()

    rst = ''
    for i in info:
        if i not in check:
            rst += i

    print("#{} {}".format(tc,rst))