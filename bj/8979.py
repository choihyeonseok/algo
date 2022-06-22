import sys
sys.stdin = open("test_input.txt")

N, K = map(int, input().split())

result = []
for tc in range(1,N+1):
    result.append(list(map(int, input().split())))
# print(result)
result.sort(key=lambda arr: (arr[1],arr[2],arr[3]))
# print(result[::-1])

for i in range(N):
    if result[::-1][i][0] == K:
        print(i+1)



