N = int(input())

arr = []
for _ in range(N):
    h = int(input())
    arr.append(h)

reverse_arr = arr[::-1]

check_arr = [arr[0]]
check_re_arr = [reverse_arr[0]]

for i in range(1,len(arr)):
    if arr[i] > check_arr[-1]:
        check_arr.append(arr[i])
    if reverse_arr[i] > check_re_arr[-1]:
        check_re_arr.append(reverse_arr[i])

print(len(check_arr))
print(len(check_re_arr))