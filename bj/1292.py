import sys
sys.stdin = open("test_input.txt")

input = sys.stdin.readline

num_list = []
rst = 0
A, B = map(int, input().split())

# print(A,B)
num = 1
while True:
    if len(num_list) >= B+1:
        break

    for i in range(num):
        num_list.append(num)

    num += 1

# print(num_list)
print(sum(num_list[A-1:B]))

