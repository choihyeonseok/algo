# 쿠폰 n
# 도장 k
# 도장 채워야 쿠폰 1장
# 한마리 시킬때마다 도장
import sys
for line in sys.stdin:
    n, k = map(int, line.split())
    result = n
    while n // k:
        result += n//k
        n = n//k + n%k
    print(result)

# while 1:
#   try:
#       n, k = map(int, input().split())
#       result = 0 
#       result += n
#       while n//k:
#           result += n//k
#           n = n//k + n%k
#       print(result)
#   except:
#       break