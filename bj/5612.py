n = int(input())
m = int(input())

plus_list = []
minus_list = []
result = []

for test_case in range(1, n + 1):
    number_in, number_out = map(int, input().split())
    plus_list.append(number_in)
    minus_list.append(number_out)

result.append(m + plus_list[0] - minus_list[0]) 

for i in range(1,n):
    result.append(result[i-1] + plus_list[i] - minus_list[i])

if -1 in result:
    rst = 0
elif max(result) < m:
    rst = m
else :
    rst = max(result)

print(rst)