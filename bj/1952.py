# M, N
# 세로 가로

M, N = map(int, input().split())

if M > N:
    result = 2*N -1
else:
    result = (M - 1) * 2

print(result)