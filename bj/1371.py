import sys
sys.stdin = open("test_input.txt")

arr = []

while True:
    try:
        s = list(map(str, input()))
        arr += s
    except:
        break
# print(arr)
# print(arr.count('a'))
result = []
english = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for eng in english:
    result.append(arr.count(eng))
# print(result)
for i in range(len(result)):
    if max(result) == result[i]:
        print(english[i],end="")


