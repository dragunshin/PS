n = int(input())
nums = list(map(int, input().split()))
what = int(input())

cnt = 0
for i in nums:
    if what == i:
        cnt += 1
print(cnt)