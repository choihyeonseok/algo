import sys
sys.stdin = open("test.txt")

N = input()

stack = []
for i in N:
    if len(stack) == 0:
        stack.append(i)
    else:
        if stack[-1] == '(' and i == ')':
            stack.pop(-1)
        else:
            stack.append(i)

if len(stack) == 0:
    print('good')
else:
    print('bad')