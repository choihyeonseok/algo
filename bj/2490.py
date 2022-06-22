import sys
sys.stdin = open("test_input.txt")

T = 3
for tc in range(1,T+1):
    result = input().split()

    # print(result)

    # 도 = A 개 = B 걸 = C 윳 = D 모 = E
    count = 0
    for i in result:
        if i == '0':
            count += 1
    # print(count)

    result_list = ['E','A','B','C','D']
    print(result_list[count])

