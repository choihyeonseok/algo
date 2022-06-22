import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    info = input()

    print('.'+'.#..'*len(info))
    print('.'+'#.#.'*len(info))
    print('#',end="")
    for i in info:
        print(".{}.#".format(i),end="")
    print()
    print('.'+'#.#.'*len(info))
    print('.'+'.#..'*len(info))
