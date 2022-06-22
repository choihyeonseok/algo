import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    a = [1,2,3,4,5,6,7,8,9]
    b = [1,2,3,4,5,6,7,8,9]
    
    rst = 'No'
    for i in a:
        for j in b:
            if i*j == N:
                rst = 'Yes'

    print("#{} {}".format(tc,rst))