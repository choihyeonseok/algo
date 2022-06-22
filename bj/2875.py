N, M, K = map(int,input().split())

Team = 0

while N >= 2 and M >= 1 and N + M >= K + 3:
    N = N - 2
    M = M - 1
    Team = Team + 1

print(Team)





# if N > M*2:
#     if N-M*2 > K :
#         N = N - K
#         K = 0
#     else :
#         K = K - (N - M*2)    

# elif N == M*2:
#     K = K       

# else:
#     if M - N//2 > K:
#         M = M - K
#         K = 0
#     else :
#         K = K - (M - N//2)

# N = N - int(K*(2/3)+0.5)
# M = M - int(K*(1/3)+0.5)

# if N > M*2:
#     result = M

# else:
#     result = N//2

# print(result)