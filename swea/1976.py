import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())

for tc in range(1,T+1):
    h1,m1,h2,m2 = map(int,input().split())

    h = h1 + h2
    if h > 12:    
        h = h - 12

    m = m1 + m2
    if m >= 60:
        m = m - 60
        h = h + 1

    print("#{} {} {}".format(tc,h,m))