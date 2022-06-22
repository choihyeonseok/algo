import sys
sys.stdin = open("exam_input.txt")

N = int(input())

check = []
rst = 0
for _ in range(N):
    n = int(input())
    check.append(n)

check.sort(reverse=True)

price = []
for i in check:
    if len(price) != 3:
        price.append(i)
    else:
        rst += price[0] + price[1]
        price = [i]

if len(price) != 3:
    rst += sum(price)
else:
    rst += price[0] + price[1]

print(rst)