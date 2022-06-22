import sys
sys.stdin = open("test_input.txt")

input = sys.stdin.readline

N = int(input())
num = []
for _ in range(N):
    x, y = map(int,input().split())
    num.append((x,y))

num.sort()
# print(num)
for i in num:
    print(i[0], i[1])
