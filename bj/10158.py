import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

w, h = map(int,input().split())
p, q = map(int,input().split())
t = int(input())

# 위치에서 턴을 더해준값을 구간으로 나누고 2로나눈 나머지
# -> 방향이면 0
if ((p+t)//w) % 2 == 0:
    # 현재위치는 초기위치에 턴을 더해주고 구간으로 나눈 나머지
    p = (p+t) % w
# <- 방향이면 1
else :
    # 현재위치는 역방향이라서 구간에서 초기위치에서 턴을 더해주고 구간으로 나눈값으로 빼줌
    p = w - ((p+t) % w)

if ((q+t)//h) % 2 == 0:
    q = (q+t) % h

else :
    q = h - ((q+t) % h)

print(p,q)

# now_x = p
# cnt_x = t

# while True:
#     if cnt_x == 0:
#         break

#     if now_x != w:
#         while now_x != w:
#             if cnt_x == 0:
#                 break

#             now_x += 1
#             cnt_x -= 1

#     else :
#         while now_x != 0:
#             if cnt_x == 0:
#                 break

#             now_x -= 1
#             cnt_x -= 1

# now_y = q
# cnt_y = t

# while True:
#     if cnt_y == 0:
#         break
    
#     if now_y != h:
#         while now_y != h:
#             if cnt_y == 0:
#                 break

#             now_y += 1
#             cnt_y -= 1

#     else :
#         while now_y != 0:
#             if cnt_y == 0:
#                 break

#             now_y -= 1
#             cnt_y -= 1

# print(now_x, now_y)