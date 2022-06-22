import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement

# from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

min_pack_price = 2147483647
min_one_price = 2147483647
for _ in range(M):
    pack_price, one_price = map(int, input().split())
    if min_pack_price > pack_price:
        min_pack_price = pack_price

    if min_one_price > one_price:
        min_one_price = one_price

# print(min_pack_price, min_one_price)

if min_pack_price <= min_one_price * 6:
    if N % 6 == 0:
        print(min_pack_price * (N//6))
    else:
        # 1. 셋트로 초과해서 사기
        # 2. 셋트 + 낱개 해서 사기
        rst1 = min_pack_price*((N//6)+1)
        rst2 = min_pack_price*(N//6) + min_one_price*(N%6)
        print(min(rst1,rst2))
else:
    print(min_one_price * N)