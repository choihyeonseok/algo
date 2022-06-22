import sys
sys.stdin = open("test_input.txt")
from itertools import permutations
# from itertools import combinations
input = sys.stdin.readline

N = sorted(list(map(str, input().rstrip())), reverse=True)

if '0' not in N:
    print(-1)
else:
    check = 0
    for i in N:
        check += int(i)

    if check % 3 != 0:
        print(-1)
    else:
        flag = 1
        for i in permutations(N, len(N)):
            # print(i)
            tmp = ''
            for j in range(len(N)):
                tmp += i[j]

            if int(tmp) % 30 == 0:
                print(int(tmp))
                flag = 0
                break

        if flag == 1:
            print(-1)