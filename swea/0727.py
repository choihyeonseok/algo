'''
# 2050
data = list(input())
for i in data:
    print(ord(i) - 64, end = ' ')

# 2047
data = input()
print(data.upper())

# 2046
a = int(input())
print('#'*a)

# 2027
for i in range(5):
    for j in range(5):
        if i == j:
            print('#', end='')
        else :
            print('+', end='')
    print()

# 2043
a, b = map(int, input().split())
print((a-b)+1)

## 1986

N = int(input())
result = 0
for i in range(1,N+1):
    
    if i % 2 == 1:
        result += i
    else :
        result -= i
print(result)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    result = 0
    for i in range(1, N+1):
        if i == 1:
            result += 1
        elif i % 2 == 1:
            result += 1
        else :
            result -= i
    print(f'#{test_case} {result}')
## 1954

## 1945

### 10804

### 10200
'''

