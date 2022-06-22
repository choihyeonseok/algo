import sys
sys.stdin = open("test_input.txt")

input = sys.stdin.readline

N = int(input())
info = list(map(int, input().split()))
# print(info, '입력')
info_list = []
for i in range(N):
    info_list.append((info[i],i))

# print(info_list)
info_list.sort()
# print(info_list)
rst = 0
for i in range(N):
    # print(N-i)
    # print(info_list[i][0] * (N-i))
    rst += info_list[i][0] * (N-i)
print(rst)