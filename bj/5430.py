import sys
sys.stdin = open("test_input.txt")
from collections import deque
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    p = input().rstrip()
    n = int(input())
    info = deque(input().rstrip()[1:-1].split(','))

    if n == 0:
        info = deque()

    reverse_check = 0
    flag = 0
    for i in p:
        # 배열 순서 뒤집기
        if i == 'R':
            reverse_check += 1
            # info.reverse()
        # 첫번째 수 버리기
        else:
            if info:
                if reverse_check % 2 == 0:
                    info.popleft()
                else:
                    info.pop()
            else:
                flag = 1
                print('error')
                break

    if flag == 0:
        if reverse_check % 2 == 0:
            print("["+",".join(info)+"]")
        else:
            info.reverse()
            print("["+",".join(info)+"]")