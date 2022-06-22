import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    rst = 0
    for _ in range(N):
        x,y = map(int,input().split())
        z = (x**2 + y**2)**0.5
        if z <= 20:
            rst += 10
        elif 20 < z <= 40:
            rst += 9
        elif 40 < z <= 60:
            rst += 8
        elif 60 < z <= 80:
            rst += 7
        elif 80 < z <= 100:
            rst += 6
        elif 100 < z <= 120:
            rst += 5
        elif 120 < z <= 140:
            rst += 4
        elif 140 < z <= 160:
            rst += 3
        elif 160 < z <= 180:
            rst += 2
        elif 180 < z <= 200:
            rst += 1            
            
    print("#{} {}".format(tc,rst))