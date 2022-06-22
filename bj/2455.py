now_list = []
now = 0
for tc in range(1,5):
    station_out, station_in = map(int,input().split())
    now += station_in - station_out
    now_list.append(now)
    
max = 0
for i in now_list:
    if max < i:
        max = i
print(max)


