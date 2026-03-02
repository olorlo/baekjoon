
from collections import deque

# 백준 1926번 그림
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    global area

    dq = deque([(y, x)])
    visited[y][x] = 1

    while dq:
        now_y, now_x = dq.popleft()

        for k in range(4):
            ny = now_y + dy[k]
            nx = now_x + dx[k]
            if nx < 0 or nx >= m or ny < 0 or ny >=n:
                continue
            if visited[ny][nx]:
                continue
            if arr[ny][nx] == 1:
                area += 1
                visited[ny][nx] = 1
                dq.append([ny, nx])

# 그림의 개수
cnt = 0
# 그림의 넓이
max_area = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j]:
            area = 1
            bfs(i, j)
            cnt += 1
            max_area = max(max_area, area)

print(cnt)
print(max_area)