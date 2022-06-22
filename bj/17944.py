N, turn = map(int, input().split())

result = []
for i in range(1,N*2+1):
    result.append(i)

real_turn = turn % ((N*4)-2)

if 0 < real_turn <= N*2:
    print(result[real_turn-1])

elif N*2 < real_turn < N*2*2:
    print(result[::-1][real_turn-(N*2)])

elif real_turn == 0:
    print(result[1])
# print(N)
# print(turns)

# 2는 1 7 13 (6) 2
# 3은 1 11 21 (10)  2
# 4는 1 15 29 (14)
# 5는 1 19 37 (18)
# (N*4)-2