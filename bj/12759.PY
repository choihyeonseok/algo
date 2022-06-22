start = int(input())

result = 0
if start == 1:
    A = 1
    B = 2
else :
    B = 1
    A = 2    

A_list = []
B_list = []
win_dict = {
    1:[[1,1],[1,2],[1,3]],
    }

while result == 0:
    A_x, A_y = map(int, input().split())
    B_x, B_y = map(int, input().split())

    A_list.append([A_x,A_y])
    B_list.append([B_x,B_y])

    # print(A_list)
    # print(B_list)

    






