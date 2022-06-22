import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

def dfs(x):
    global rst
    if x == N:
        rst += 1
        return

    for i in range(N):
        visited[x] = i
        for j in range(x):
            if visited[j] == visited[x]:
                break
            if abs(visited[j]-visited[x]) == (x-j):
                break
        else:
            dfs(x+1)


# T = int(input())
# for tc in range(1,T+1):
N = int(input())
rst = 0
visited = [0]*N

dfs(0)
print(rst)
# print("#{} {}".format(tc, rst))
