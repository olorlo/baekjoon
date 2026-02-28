import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

from collections import deque

# 백준 2178번 미로탐색
N, M = map(int, input().split())
# 엔터 포함되어있는 것은 strip()으로 제거
maze = [input().strip() for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    dq = deque([(y, x)])
    visited[y][x] = 1
    while dq:
        now_y, now_x = dq.popleft()

        for k in range(4):
            ny = now_y + dy[k]
            nx = now_x + dx[k]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            if not visited[ny][nx] and int(maze[ny][nx]):
                # visited에 현재 거리 + 1 씩 해주면서 거리 더 해감
                visited[ny][nx] = visited[now_y][now_x] + 1
                dq.append([ny, nx])

visited = [[0] * M for _ in range(N)]
bfs(0,0)
print(visited[N-1][M-1])