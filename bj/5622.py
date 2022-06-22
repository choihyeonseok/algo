import sys
sys.stdin = open("test_input.txt")

T = 2

for tc in range(1,T+1):
    print(tc)
    words = input()
    buttons = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    result = 0
    for word in range(len(words)):
        for button in range(len(buttons)):
            if words[word] in buttons[button]:
                result += button + 3
    print(result)
