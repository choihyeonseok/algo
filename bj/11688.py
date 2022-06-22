import sys
sys.stdin = open("test_input.txt")

T = int(input())
for tc in range(1, T+1):
    test = input()

    rst_a = 1
    rst_b = 1
    for i in test:
        if i == 'L':
            rst_b = rst_a + rst_b
        else:
            rst_a = rst_a + rst_b

    print("#{} {} {}".format(tc, rst_a, rst_b))