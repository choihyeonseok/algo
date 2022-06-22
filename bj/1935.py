import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

N = int(input())
info = list(map(str,input().rstrip()))

alphabet = []
for _ in range(N):
    alphabet.append(int(input()))

rst = 0
tmp = []
for i in info:
    # 연산자가 아닐때
    if i != '*' and i != '+' and i != '-' and i != '/':
        tmp.append(alphabet[ord(i) - 65])
    # 연산자 일때
    else:
        num1 = tmp.pop(-2)
        num2 = tmp.pop(-1)
        if i == '+':
            tmp.append(num1 + num2)
        if i == '-':
            tmp.append(num1 - num2)
        if i == '*':
            tmp.append(num1 * num2)
        if i == '/':
            tmp.append(num1 / num2)

print("%.2f"%tmp[0])