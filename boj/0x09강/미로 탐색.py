from collections import deque

N,M = map(int, input().split())
route = [list(map(int,input())) for _ in range(N)]

start = (0,0)
end = (N-1,M-1)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = []
def bfs():
    q = deque()
    q.append(start)

    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny <0 or ny >= M: continue
            if route[nx][ny] == 1:
                route[nx][ny] = route[x][y] + 1
                q.append((nx,ny))
    return route[N-1][M-1]

print(bfs())