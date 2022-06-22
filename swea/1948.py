import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

# month_info = [0,1,2,3,4,5,6,7,8,9,10,11,12]
day_info = [0,31,28,31,30,31,30,31,31,30,31,30,31]

T = int(input())
for tc in range(1,T+1):
    s_m, s_d, e_m, e_d = map(int,input().split())  

    rst = 0
    if s_m == e_m:
        rst = e_d - s_d + 1

    else:
        for i in range(s_m+1,e_m):
            rst += day_info[i]
        
        rst += day_info[s_m] - s_d + e_d + 1

    print("#{} {}".format(tc,rst))