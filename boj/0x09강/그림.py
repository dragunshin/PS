from collections import deque
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

draw = []
result = []
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(paper, x, y):
    q = deque()
    q.append((x,y))
    paper[x][y] = 0
    cnt = 1
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if paper[nx][ny] == 1:
                paper[nx][ny] = 0
                q.append((nx,ny))
                cnt += 1
    return cnt

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            result.append(bfs(paper,i,j))
            
if len(result) == 0:
    print(0)
    print(0)
else:
    print(len(result))
    print(max(result))