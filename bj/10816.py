import sys
sys.stdin = open("test_input.txt")

input = sys.stdin.readline

N = int(input())
cards = list(map(int,input().split()))

M = int(input())
check = list(map(int,input().split()))

plus = [0] * 10000001
minus = [0] * 10000001

# plus = [0] * 11
# minus = [0] * 11
for i in cards:
    if i >= 0:
        plus[i] += 1
    else:
        minus[i*(-1)] += 1

# print(plus)
# print(minus)
#
# print(cards)
# print(check)

rst = []
for i in check:
    if i >= 0:
        rst.append(plus[i])
    else:
        rst.append(minus[i*(-1)])

print(*rst)
