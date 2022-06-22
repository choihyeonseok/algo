import sys
sys.stdin = open("test_input.txt")

for tc in range(1, 11):
    N = int(input())
    test = input()
    rst = 0
    for i in test:
        if i == '+':
            pass
        else:
            rst += int(i)

    print("#{} {}".format(tc, rst))
