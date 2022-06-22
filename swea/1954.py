# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())

#     for i in range(N):
#         for j in range(N):
#             pass


#     # print(f'#{test_case}')
#     print(result)

################################################

N = int(input())

result = ''
if N % 2 != 0:
    pass
    for i in range(N):
        # print(N-i)
        result += f'{N-i}'
    print(' '.join(result[::-1]))

else :
    pass