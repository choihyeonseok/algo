import sys
sys.stdin = open("test_input.txt")

def dfs(num):
    global cnt
    check[num] = 1

    for w in range(1, computer+1):
        if arr[num][w] == 1 and check[w] == 0:
            dfs(w)
            cnt += 1


computer = int(input())
networks = int(input())

arr = [[0] * (computer+1) for _ in range(computer+1)]
check = [0] * (computer+1)
cnt = 0

for network in range(networks):
    num1, num2 = map(int,input().split())
    arr[num1][num2] += 1
    arr[num2][num1] += 1

dfs(1)

print(cnt)