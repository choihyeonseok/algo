import sys
sys.stdin = open("test.txt")

N = int(input())
num = input()
rst = [num[-1]]
cnt = 1

for i in range(N-2,-1,-1):
    rst.append(num[i])
    cnt += 1
    if cnt == 3 and i != 0:
        rst.append(',')
        cnt = 0
        
for i in rst[::-1]:
    print(i,end="")