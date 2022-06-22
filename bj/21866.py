import sys
sys.stdin = open("test_input.txt")

N, M = map(int,input().split())

result_t = 0
for tc in range(N):
    t_in, t_out = map(int,input().split())
    if t_in == t_out:
        result_t += 1

result_s = 0
for sc in range(M):
    s_in, s_out = map(int,input().split())
    if s_in == s_out:
        result_s += 1

if result_t == N and result_s == M:
    print('Accepted')
elif result_t != N:
    print('Wrong Answer')
else:
    print('Why Wrong!!!')
