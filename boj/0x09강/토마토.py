from collections import deque

M,N = map(int, input().split())
tomato = [list(map(int,input().split())) for _ in range(N)]

after = [[-1]*M for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

#def bfs(x,y):
q = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            after[i][j] = 0
            q.append((i,j))
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if tomato[nx][ny] == 0 and after[nx][ny] == -1:
            after[nx][ny] = after[x][y] + 1
            q.append((nx,ny))
day = 0
is_ = False
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0 and after[i][j] == -1:
            is_ = True
            break
        day = max(day, after[i][j])
    if is_:
        break
if is_: print(-1)
else: print(day)
        