import sys
sys.stdin = open("exam_input.txt")
input = sys.stdin.readline


# n_list = [0,1,2,4,7,13,24,44,81,149,274]
n_list = [0,1,2,4] + [0]*1000000
for i in range(4,1000001):
    n_list[i] = (n_list[i-1]+n_list[i-2]+n_list[i-3]) % 1000000009
T = int(input())
for _ in range(T):
    n = int(input())
    print(n_list[n])