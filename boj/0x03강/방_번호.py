room = list(input())

cnt = [0] * 10
for ch in room:
    # if (room[i] == '6' or room[i] == '9') and cnt[6] != cnt[9]:
    if ch in ('6','9') and cnt[6] != cnt[9]:
        if cnt[6] < cnt[9]:
            cnt[6] += 1
        else:
            cnt[9] += 1
    else:
        cnt[int(ch)] += 1
print(max(cnt))