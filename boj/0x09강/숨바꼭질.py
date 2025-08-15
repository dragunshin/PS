from collections import deque
a,b = map(int, input().split())

def bfs(a,b):
    q = deque([a])
    while q:
        x = q.popleft()
        if x == b: 
            print(dist[x])
            break
        for dir in (x-1,x+1,x*2):
            if 0 <= dir < 100001 and dist[dir] == 0:
                dist[dir] = dist[x] + 1
                q.append(dir)


dist = [0] * 100001
bfs(a,b)