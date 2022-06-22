import sys
sys.stdin = open("test_input.txt")

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    cards = list(map(int,input().split()))
    card_sum = []
    for i in range(N):
        for j in range(i,N):
            for k in range(j,N):
                if cards[i] + cards[j] + cards[k] <= M and i!=j!=k:
                    card_sum.append(cards[i] + cards[j] + cards[k])
    max = 0
    for i in card_sum:
        if i > max:
            max = i
    print(max)
