import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
input = sys.stdin.readline

S = input().rstrip()
tmp = []
cnt_one = 0
cnt_zero = 0
for i in S:
    # print(i)
    if len(tmp) == 0:
        tmp.append(i)
        if i == '1':
            cnt_one += 1
        else:
            cnt_zero += 1
    else:
        if tmp[-1] != i:
            tmp.append(i)
            if i == '1':
                cnt_one += 1
            else:
                cnt_zero += 1

# print(tmp)
# print(cnt_one)
# print(cnt_zero)

print(min(cnt_one, cnt_zero))

