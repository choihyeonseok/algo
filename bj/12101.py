import sys
sys.stdin = open("test_input.txt")
# from itertools import permutations
# from itertools import combinations
from itertools import product
# from itertools import combinations_with_replacement
input = sys.stdin.readline


N, K = map(int, input().split())
num = [1,2,3]
rst = []
for n in list(range(1,N+1)):
    for i in product(num, repeat = n):
        if sum(i) == N:
            # print(i, sum(i))
            rst.append(list(i))

rst.sort()
# print(rst)
if K > len(rst):
    print(-1)
else:
    result = rst[K-1]
    # print(result)
    rst = ''
    for i in result:
        rst += str(i)+'+'

    print(rst[:-1])

