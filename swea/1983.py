import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())
    scores = []
    for _ in range(N):
        score = list(map(int,input().split()))
        total_score = score[0]*0.35 + score[1]*0.45 + score[2]*0.20
        scores.append(total_score)
    check = scores[K-1]
    scores.sort()
    for i in range(N):
        if check == scores[::-1][i]:
            rank = i+1
    grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    rst = []
    for i in grade:
        for _ in range(N//10):
            rst.append(i)
    print("#{} {}".format(tc,rst[rank-1]))