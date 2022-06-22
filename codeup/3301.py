import sys
sys.stdin = open("test.txt")

N = int(input())

money = [50000,10000,5000,1000,500,100,50,10]

cnt = 0
for i in money:
    while True:
        if N - i >= 0:
            N -= i
            cnt += 1        
        else:
            break

print(cnt)