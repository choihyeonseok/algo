T = input()
# print(len(T))
count = 0
for i in T:
    # print(i)
    if type(i) == str:
        count += 1
print(count)