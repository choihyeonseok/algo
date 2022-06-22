import sys
sys.stdin = open("test_input.txt")

C = int(input())

for tc in range(1,C+1):
    scores = list(map(int,input().split()))
    N = scores[0]
    score = 0
    for i in range(1,len(scores)):
        score += scores[i]
    # print(score)
    avg = score / N
    # print(avg)

    count = 0
    for i in range(1,len(scores)):
        if scores[i] > avg:
            count += 1

    result = count / N * 100
    print("{:.3f}%".format(result))

