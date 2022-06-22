num1 = int(input())
num2 = str(input())

print(num2[::-1])

for i in range(len(num2)):
    print(int(num2[::-1][i])*num1)

print(num1* int(num2))