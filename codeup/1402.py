import sys
sys.stdin = open("test.txt")

n = int(input())

arr = list(map(int,input().split()))

print(*arr[::-1])