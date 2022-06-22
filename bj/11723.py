import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

M = int(input())

S = []
for _ in range(M):
    try:
        info = input().rstrip().split()
    except:
        info = input().rstrip()

    if info[0] == 'add':
        if int(info[1]) not in S:
            S.append(int(info[1]))

    if info[0] == 'remove':
        if int(info[1]) in S:
            S.remove(int(info[1]))

    if info[0] == 'check':
        if int(info[1]) in S:
            print(1)
        else:
            print(0)

    if info[0] == 'toggle':
        if int(info[1]) in S:
            S.remove(int(info[1]))
        else:
            S.append(int(info[1]))

    if info[0] == 'all':
        S = list(range(1,21))

    if info[0] == 'empty':
        S = []