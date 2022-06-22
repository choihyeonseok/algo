T = int(input())

for test_case in range(1, T + 1):
    a = str(input())

    year = a[0:4]
    month = a[4:6]
    date = a[6:8]

    date_list = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']

    month_list_31 = ['01','03','05','07','08','10','12']
    month_list_30 = ['04','06','09','11']

    if month in month_list_31 and date in date_list:
        print(f'#{test_case} {a[0:4]}/{a[4:6]}/{a[6:8]}')
    elif month in month_list_30 and date in date_list[0:30]:
        print(f'#{test_case} {a[0:4]}/{a[4:6]}/{a[6:8]}')
    elif month == '02' and date in date_list[0:28]:
        print(f'#{test_case} {a[0:4]}/{a[4:6]}/{a[6:8]}')
    else :
        print(f'#{test_case} -1')
