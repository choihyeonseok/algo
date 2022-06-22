import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline


T = int(input())
for tc in range(1,T+1):
    # N, K = map(int,input().split())
    N_list = list(map(int,input().split()))
    check = []


    for i in range(7):
        # print(N_list[i])
        for j in range(i+1,7):
            # print(N_list[j])
            for k in range(j+1,7):
                # print(N_list[k])
                # print(N_list[i]+N_list[j]+N_list[k])
                if N_list[i]+N_list[j]+N_list[k] not in check:
                    check.append(N_list[i]+N_list[j]+N_list[k])

    check.sort(reverse=True)
    # print(check)
    rst = check[4]

    print("#{} {}".format(tc, rst))
