import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

N = int(input())
cnt = 0
checks = []
for tc in range(N):
    arr = list(map(int,input().split()))
    if arr[0] == 1:
        arr[2] -= 1
        if arr[2] == 0:
            cnt += arr[1]
        else:
            checks.append([arr[1],arr[2]])
    
    else:
        if len(checks) != 0:
            checks[-1][-1] -= 1
            if checks[-1][-1] == 0:
                cnt += checks[-1][0]
                checks.pop()

print(cnt)