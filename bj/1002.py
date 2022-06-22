import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
input = sys.stdin.readline

N = int(input())

for i in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)

    else:
        dist = ((abs(x1-x2) ** 2) + (abs(y1-y2) ** 2))
        r = r1 + r2

        if(dist == r**2 or dist == abs(r2 - r1)**2):
            print(1)
        elif(dist > r**2 or dist < abs(r2 - r1)**2):
            print(0)
        else:
            print(2)
