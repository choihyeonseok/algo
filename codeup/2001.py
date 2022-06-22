import sys
sys.stdin = open("test.txt")

p1 = int(input())
p2 = int(input())
p3 = int(input())
j1 = int(input())
j2 = int(input())

p = min(p1,p2,p3)
j = min(j1,j2)

rst = (p + j)*1.1

print(format(rst,".1f"))