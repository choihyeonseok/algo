import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())

for tc in range(1,T+1):
    case = input()
    arr = []
    i = 0
    while True:
        if len(arr) == 0:
            arr.append(case[i])
        else:
            if arr[0] != case[i]:
                arr.append(case[i])
            else:
                if arr[1] == case[i+1]:
                    break
                else:
                    arr.append(case[i])
        i += 1
        
    print("#{} {}".format(tc,len(arr)))
    