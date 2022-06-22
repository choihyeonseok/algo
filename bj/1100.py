import sys
sys.stdin = open("test_input.txt")

count = 0
for tc in range(8):
    T = input()
    for i in range(len(T)):
        if tc % 2 == 0 and i % 2 == 0 and T[i] != '.' :
            count += 1
        elif tc % 2 != 0 and i % 2 != 0 and T[i] != '.':
            count += 1
print(count)