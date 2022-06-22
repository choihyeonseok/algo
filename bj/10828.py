import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    try:
        info = input().split()

    except:
        info = input()

    if info[0] == 'push':
        stack.append(info[1])

    if info[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(-1))

    if info[0] == 'size':
        print(len(stack))

    if info[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    if info[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])