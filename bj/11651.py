import sys
sys.stdin = open("test_input.txt")

input = sys.stdin.readline

N = int(input())
num = []
for _ in range(N):
    x, y = map(int,input().split())
    num.append((y,x))

num.sort()
# print(num)
for i in num:
    print(i[1], i[0])
