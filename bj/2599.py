import sys
sys.stdin = open("test_input.txt")
input = sys.stdin.readline

N = int(input())
Am, Aw = map(int,input().split())
Bm, Bw = map(int,input().split())
Cm, Cw = map(int,input().split())

for i in range(Am+1):
    AmBw = i

    AmCw = Am - AmBw

    BmCw = Cw - AmCw

    BmAw = Bm - BmCw

    CmAw = Aw - BmAw

    CmBw = Cm - CmAw  
    

    if Am >= 0 and Aw >= 0 and Bm >= 0 and Bw >= 0 and Cm >= 0 and Cw >= 0:
        print(1)
        print(AmBw, AmCw)
        print(BmAw, BmCw)
        print(CmAw, CmBw)
        break

if Am or Bm or Cm or Aw or Bw or Cw:
    print(0)

# if Am == 0 and Aw == 0 and Bm == 0 and Bw == 0 and Cm == 0 and Cw == 0:
#     print(1)
#     print(AmBw, AmCw)
#     print(BmAw, BmCw)
#     print(CmAw, CmBw)

# else:
#     print(0)