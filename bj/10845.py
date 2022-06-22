import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement
input = sys.stdin.readline

N = int(input())
Q = []
for _ in range(N):
    try:
        info = input().split()
    except:
        info = input()

    # print(info)

    if info[0] == 'push':
        Q.append(info[1])
    elif info[0] == 'pop':
        if Q:
            print(Q.pop(0))
        else:
            print(-1)
    elif info[0] == 'size':
        print(len(Q))
    elif info[0] == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    elif info[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    else:
        if Q:
            print(Q[-1])
        else:
            print(-1)

