import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
input = sys.stdin.readline

N = int(input())
# max_value = 0
rst = []
for i in range(N, -1, -1):
    # print(N, i, N-i)
    check = [N, i]
    while check[-1] >= 0:
        check.append(check[-2] - check[-1])

    # if max_value < len(check):
    #     max_value = len(check)
    # print(check)
    rst.append((len(check), check))

# print(max_value-1)
rst.sort()
print(rst[-1][0]-1)
print(*rst[-1][-1][:rst[-1][0]-1])