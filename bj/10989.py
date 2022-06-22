import sys
sys.stdin = open("test_input.txt")

input = sys.stdin.readline

N = int(input())
num = [0]*10001
for _ in range(N):
    n = int(input())
    num[n] += 1

print(num)

for i in range(10001):
    # print(num[i])
    if num[i] != 0:
        print(num[i],i)