import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    S = list(input())
    
    check = []
    
    for i in S:
        if i != '\n' and i not in check:
            check.append(i)

    cnt = [0] * len(check)
    for i in S:        
        for j in range(len(check)):            
            if i == check[j]:
                cnt[j] += 1

    rst = 'Yes'
    for i in cnt:
        if i != 2:
            rst = 'No'                

    print("#{} {}".format(tc,rst))