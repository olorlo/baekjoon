import sys
# sys.setrecursionlimit(10**6)
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline 

from collections import deque

# 백준 2206 벽 부수고 이동하기
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[-1]*2 for _ in range(M)] for _ in range(N)]

def bfs(y, x, c):
    dq = deque([(y, x, c)])
    visited[y][x][c] = 1

    while dq:
        now_y, now_x, cnt = dq.popleft()

        if (now_y, now_x) == (N-1, M-1):
            return visited[now_y][now_x][cnt]

        for k in range(4):
            ny = now_y + dy[k]
            nx = now_x + dx[k]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            if arr[ny][nx] == 0:
                if visited[ny][nx][cnt] != -1:
                    continue
                visited[ny][nx][cnt] = visited[now_y][now_x][cnt] + 1
                dq.append((ny, nx, cnt))

            # 벽 부수기
            elif cnt == 0 and arr[ny][nx] == 1:
                if visited[ny][nx][1] != -1:
                    continue
                visited[ny][nx][1] = visited[now_y][now_x][cnt] + 1
                dq.append((ny, nx, cnt+1))
            
    return -1

result = bfs(0, 0, 0)
print(result)