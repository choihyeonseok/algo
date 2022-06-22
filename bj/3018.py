import sys
sys.stdin = open("exam_input.txt")
input = sys.stdin.readline


N = int(input())
E = int(input())

check_num = [[] for _ in range(N)]

print(check_num)

for _ in range(E):
    arr = list(map(int,input().split()))
    arr.pop(0)
    print(arr)
    if 1 in arr:
        for i in arr:
            # print(i-1)
            check_num[i-1].append('*')

    else:
        tmp = 0
        for i in arr:
            if tmp < len(check_num[i-1]):
                tmp = len(check_num[i-1])
                tmp_change = check_num[i-1]

        for j in arr:
            check_num[j-1] = tmp_change
        print(tmp_change)

    print(check_num)


