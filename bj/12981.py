import sys

sys.stdin = open("test_input.txt")
input = sys.stdin.readline

r,g,b = map(int,input().split())
cnt = 0

start = min(r,g,b)

r -= start
g -= start
b -= start

cnt += start

if r != 0:
    cnt += r // 3
    r = r % 3

if g != 0:
    cnt += g // 3
    g = g % 3

if b != 0:
    cnt += b // 3
    b = b % 3

if r == 0:
    check = [g,b]
if g == 0:
    check = [r,b]
if b == 0:
    check = [r,g]

last = min(check)

cnt += last    

if r != 0:
    r -= last

if g != 0:
    g -= last

if b != 0:
    b -= last

if r != 0 or g != 0 or b != 0:
    r =0
    g =0
    b =0
    cnt += 1

print(cnt)