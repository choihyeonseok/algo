X = int(input())

turn = 1

while X > turn:
    X -= turn
    turn += 1

if turn % 2 == 0:
    a = X
    b = turn - X + 1
else :
    a = turn - X + 1
    b = X

print(f'{a} / {b}')