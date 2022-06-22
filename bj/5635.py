import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

n = int(input())
check = []
for _ in range(n):
    name, day, month, year = map(str, input().split())
    check.append((int(year), int(month), int(day), name))

# print(check)
check.sort()
# print(check)

print(check[-1][-1])
print(check[0][-1])
