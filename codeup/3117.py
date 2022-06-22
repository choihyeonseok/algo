import sys
sys.stdin = open("test.txt")

N = int(input())

rst = []
for _ in range(N):
    num = int(input())
    if num != 0:
        rst.append(num)
    else:
        rst.pop(-1)

print(sum(rst))