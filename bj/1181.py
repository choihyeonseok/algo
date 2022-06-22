import sys
sys.stdin = open("test_input.txt")

input = sys.stdin.readline

N = int(input())
words = []
for _ in range(N):
    word = input().rstrip()
    if word not in words:
        words.append(word)

words.sort()
# print(words)
# print(sorted(words, key=len))
for i in sorted(words, key=len):
    print(i)