from collections import deque

N,M = map(int,input().split())
r,c,d = map(int,input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
room = [list(map(int,input().split())) for _ in range(N)]

cnt = 0
while True:
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1
    
    move = False
    for _ in range(4):
        d = (d + 3) % 4
        nr = r + dx[d]
        nc = c + dy[d]
        if (0 <= nr < N and 0 <= nc < M) and room[nr][nc] == 0:
            r,c = nr,nc
            move = True
            break
    if move:
        continue
    
    nr = r - dx[d]
    nc = c - dy[d]
    if (0 <= nr < N and 0 <= nc < M) and room[nr][nc] != 1:
        r,c = nr,nc
    else: break
        
print(cnt)