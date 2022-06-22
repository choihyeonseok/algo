num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1==num2==num3==60:
    print('Equilateral')

elif num1+num2+num3 == 180:
    if num1==num2:
        print('Isosceles')
    elif num2==num3:
        print('Isosceles')
    elif num1==num3:
        print('Isosceles')
    else :
        print('Scalene')
elif num1+num2+num3 != 180:
    print('Error')