import sys
sys.stdin = open("exam_input.txt")
input = sys.stdin.readline





# arr = list(range(1,N+1))
while True:
    arr = list(map(int,input().split()))

    if len(arr) == 1:
        break

    N = arr.pop(0)
    # print(arr,N)
    for a in range(N):
        # print(a)
        for b in range(a + 1, N):
            for c in range(b+1,N):
                for d in range(c + 1, N):
                    for e in range(d + 1, N):
                        for f in range(e + 1, N):
                            print(arr[a],arr[b],arr[c],arr[d],arr[e],arr[f])
    print()
