N = int(input())
seat = input()

result = 0

result += seat.count('S')
result += seat.count('L')//2

if 'L' not in seat:
    print(N)
else :
    print(result+1)