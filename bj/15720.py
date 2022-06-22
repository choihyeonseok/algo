import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

B, C, D = map(int, input().split())
bugers = list(map(int, input().split()))
sides = list(map(int, input().split()))
drinks = list(map(int, input().split()))

bugers.sort(reverse=True)
sides.sort(reverse=True)
drinks.sort(reverse=True)

# print(bugers)
# print(sides)
# print(drinks)

set_cnt = min(B,C,D)
# print(set_cnt)

rst = 0
for i in range(set_cnt):
    rst += (bugers[i] + sides[i] + drinks[i]) * 0.9

rst += sum(bugers[set_cnt::])
rst += sum(sides[set_cnt::])
rst += sum(drinks[set_cnt::])

print(sum(bugers)+sum(drinks)+sum(sides))
print(int(rst))
