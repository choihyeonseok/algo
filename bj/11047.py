import sys
sys.stdin = open("exam_input.txt")

N, K = map(int, input().split())
money = []
for _ in range(N):
    money.append(int(input()))

money.sort(reverse=True)

cnt = 0
for i in money:
    if K >= i:
        while True:
            if K - i >= 0:
                K -= i
                cnt += 1
            else:
                break
        if K == 0:
            print(cnt)
            break




