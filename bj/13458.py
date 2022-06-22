import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B, C = map(int,input().split())

cnt = 0
for i in A:
    # 총 감독관이 감당 가능한 경우
    if i <= B:
        cnt += 1
    # 총 감독관이 감당 불가능한 경우 / 부감독관도 붙어야함
    else:
        i -= B
        cnt += 1
        # 부감독관이 나누어 떨어질 때
        if i % C == 0:
            cnt += i//C
        # 아닐 때
        else:
            cnt += int(i/C+1)

print(cnt)