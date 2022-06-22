import sys
sys.stdin = open("test_input.txt")

T = 3
for tc in range(T):
    p1, p2, p3, p4, p5, p6, p7, p8, p9 = map(int, input().split())
    result = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9

    if p1 > 100 or p2 > 100 or p3 > 200 or p4 > 200 or p5 > 300 or p6 > 300 or p7 > 400 or p8 > 400 or p9 > 500:
        print('hacker')
    else:
        if result < 100:
            print('none')
        elif result <= 2500:
            print('draw')