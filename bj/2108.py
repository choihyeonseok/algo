import sys
from collections import Counter
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

N = int(input())

check = []
for _ in range(N):
    info = int(input())
    # print(info)
    check.append(info)

# print(check)
check.sort()
# print(check)


if sum(check)/N < 0:
    print(int(sum(check)/N-0.5))
else:
    print(int(sum(check)/N+0.5))
print(check[int(N/2)])
# print('최빈')
cnt = Counter(check).most_common(2)
# print(cnt)
if len(check) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(abs(min(check)-max(check)))
