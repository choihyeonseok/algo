import sys
sys.stdin = open("test_input.txt")

input = sys.stdin.readline

N = int(input())
rst = 1
check = list(range(1,N+1))
for i in check:
    rst *= i
rst = str(rst)
# print(rst)
cnt = 0
for i in range(len(rst)-1,-1,-1):
    # print(rst[i])
    if rst[i] == '0':
        cnt += 1
    else:
        break

print(cnt)