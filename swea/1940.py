import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    speed = 0
    distance = 0
    check = []
    for _ in range(N):
        arr = list(map(int,input().split()))
        if len(arr) != 1:
            check.append(arr)
        else:
            if len(check) != 0:
                arr.append(check[-1][-1])
                check.append(arr)

    for i in check:
        command = i[0]
        value = i[1]

        if command == 1:
            speed += value

        if command == 2:
            speed -= value
            if speed < 0:
                speed = 0

        distance += speed
    
    print("#{} {}".format(tc, distance))