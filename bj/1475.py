import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline
N = list(map(int, input().rstrip()))
check = [0] * 10
new_check = [0] * 10
for i in N:
    check[i] += 1
for i in range(10):
    if i == 6:
        new_check[9] += check[i]
    elif i == 9:
        new_check[i] += check[i]
        if new_check[i] % 2 == 0:
            new_check[i] //= 2
        else:
            new_check[i] -= 1
            new_check[i] //= 2
            new_check[i] += 1
    else:
        new_check[i] += check[i]
print(max(new_check))