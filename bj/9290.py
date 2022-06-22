import sys
sys.stdin = open("exam_input.txt")

T = int(input())

for tc in range(1,T+1):
    # 입력
    info = [list(map(str,input())) for _ in range(3)]
    stone = input()

    # 좌표 p 리스트 (튜플)
    p = []
    for i in range(3):
        for j in range(3):
            if info[i][j] == stone:
                p.append((i,j))

    # 앞자리(i)가 같을 때 (가로)
    if p[0][0] == p[1][0]:
        info[p[0][0]][0] = info[p[0][0]][1] = info[p[0][0]][2] = stone
        # print(p)

    # 뒷자리(j)가 같을 때 (세로)
    elif p[0][1] == p[1][1]:
        info[0][p[0][1]] = info[1][p[0][1]] = info[2][p[0][1]] = stone
        # print(p)

    # 앞 뒤 모두 다를때 (대각선)
    else:
        if (0,0) in p or (2,2) in p:
            info[0][0] = info[1][1] = info[2][2] = stone
        elif (0,2) in p or (2,0) in p:
            info[0][2] = info[1][1] = info[2][0] = stone
        # print(p)

    # 출력
    print('Case {}:'.format(tc))
    for i in range(3):
        for j in range(3):
            print(info[i][j], end="")
        print()