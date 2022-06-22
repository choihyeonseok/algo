import sys
sys.stdin = open("test_input.txt")

N = int(input())
nums = list(map(int,input().split()))

max = nums[0]
min = nums[0]
for num in nums:
    if max < num:
        max = num
    if min > num:
        min = num

print(min,max)