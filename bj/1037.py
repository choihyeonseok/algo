import sys
sys.stdin = open("exam_input.txt")
input = sys.stdin.readline


N = int(input())

arr = list(map(int,input().split()))
if N == 1:
    print(arr[0]**2)
else:
    # print(arr)
    print(min(arr)*max(arr))
