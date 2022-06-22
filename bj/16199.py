year, month, date = map(int,input().split())

now_year, now_month, now_date = map(int,input().split())

# 만나이 : 국제적인 표준 방법이다. 한국에서도 법에서는 만 나이만을 사용한다.
# 세는 나이 : 한국에서 보통 나이를 물어보면 세는 나이를 의미한다.
# 연나이 : 법률에서 일괄적으로 사람을 구분하기 위해서 사용하는 나이이다.

if month < now_month:
    man_years = now_year - year

elif month == now_month:
    if date <= now_date:
        man_years = now_year - year
    else:
        man_years = now_year - year - 1

else:
    man_years = now_year - year - 1
print(man_years)

count_years = now_year - year + 1
print(count_years)

year_years = now_year - year
print(year_years)