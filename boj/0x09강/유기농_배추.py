from collections import deque

T = int(input())
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def bfs(ground,M,N,i,j):
    q = deque([(i,j)])
    ground[i][j] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if ground[nx][ny] == 1:
                ground[nx][ny] = 0
                q.append((nx,ny))
                 
for i in range(T):
    M,N,K = map(int, input().split())
    ground = [[0]*M for _ in range(N)]
    for _ in range(K):
        x,y = map(int, input().split())
        ground[y][x] = 1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1:
                bfs(ground,M,N,i,j)
                cnt += 1
    
    print(cnt)
    