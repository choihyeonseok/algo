import sys
sys.stdin = open("exam_input.txt")
input = sys.stdin.readline

A, B, C = map(int, input().split())
print((A**B)%C)
print(pow(A,B,C))