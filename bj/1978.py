import sys
sys.stdin = open("exam_input.txt")

N = int(input())
nums = list(map(int, input().split()))
cnt = 0
for i in nums:
    if i != 1:
        for j in range(2,i+1):
            if i % j == 0:
                if j == i:
                    cnt += 1
                break
print(cnt)