import sys
sys.stdin = open("test_input.txt")

input = sys.stdin.readline

N = list(map(str,input()))
N.sort()
N = N[::-1]
# print(N)
rst = ''
for i in N:
    rst += i
print(rst)