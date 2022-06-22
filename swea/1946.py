import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    result = []
    rst = []
    for _ in range(N):
        arr = list(input().split())
        word = arr[0]
        cnt = int(arr[-1])
        for _ in range(cnt):
            result.append(word)
            if len(result) == 10:
                rst.append(result)
                result = []
    rst.append(result)
    print("#{}".format(tc))
    for i in rst:
        for j in range(len(i)):
            print(i[j],end="")
        print()