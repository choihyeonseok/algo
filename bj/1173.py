# N 운동하는시간 
# m 최소맥박 이하시 m 50
# M 최대맥박 200
# T 운동할경우 이만큼 증가
# R 운동안하면 이만큼 감소

# N분만큼 운동하는데 필요한 시간의 최솟값은?

N, m, M, T, R = map(int, input().split())

count_T = 0
count_rst = 0
pulse_now = m

if pulse_now + T > M:
    count_rst = -1
else:
    while count_T != N:
        if pulse_now + T <= M:
            pulse_now += T
            count_T += 1
            count_rst += 1
        else :
            pulse_now -= R
            count_rst += 1
            if pulse_now < m:
                pulse_now = m 
print(count_rst)
        # print(pulse_now)



    

        
    
    

    

    
    






# print(f'{N} {m} {M} {T} {R}')