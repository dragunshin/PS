n, k = map(int, input().split())

cnt = [[0]*6 for _ in range(2)] # 0 girl 1 boy

for i in range(n):
    sex, age = map(int, input().split())
    cnt[sex][age-1] += 1

room = 0

for i in range(2):
    for j in range(6):
        if cnt[i][j] % k == 0:
            room += (cnt[i][j]//k)
        else:
            room += (cnt[i][j]//k + 1)
            
print(room)