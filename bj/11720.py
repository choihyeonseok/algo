import sys
sys.stdin = open("test_input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    numbers = input()
    result = 0
    for number in range(len(numbers)):
        result += int(numbers[number])
    print(result)
