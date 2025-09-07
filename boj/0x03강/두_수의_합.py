n = int(input())
nums = list(map(int, input().split()))
x = int(input())
nums_set = set(nums)
cnt = 0

for i in nums:
    j = x - i
    if j in nums_set:
        cnt += 1
        
print(cnt//2)