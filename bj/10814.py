import sys
sys.stdin = open("test_input.txt")

input = sys.stdin.readline

N = int(input())
info = []
for _ in range(N):
    year, name = map(str,input().split())
    info.append((int(year),name))

# print(info)
# print(sorted(info, key=lambda x:x[0]))

for i in sorted(info, key=lambda x:x[0]):
    print(i[0], i[1])
