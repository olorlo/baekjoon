import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

from collections import deque

# 백준 10026번 적록색약
N =int(input())
picture = [list(input().strip()) for _ in range(N)]

visited_rgb = [[0] * N for _ in range(N)]
visited_rb = [[0] * N for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x, visited, mode):
    dq = deque([(y, x)])
    visited[y][x] = 1

    while dq:
        now_y, now_x = dq.popleft()
        now_color = picture[now_y][now_x]

        for k in range(4):
            ny = now_y + dy[k]
            nx = now_x + dx[k]

            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue

            if visited[ny][nx]:
                continue

            next_color = picture[ny][nx]
            
            # 일반인일때 
            if mode == 1:
                if now_color == next_color:
                    visited[ny][nx] = 1 
                    dq.append([ny, nx])

            # 색약일 때
            else:
                # 현재 컬러가 다음 컬러와 같거나 
                # 현재나 다음 컬러가 red나 green 인 경우
                if now_color == next_color or \
                    (now_color in 'RG' and next_color in 'RG'):
                    visited[ny][nx] = 1
                    dq.append([ny, nx])

rgb = 0 
rb = 0

# 일반
for y in range(N):
    for x in range(N):
        if not visited_rgb[y][x]:
            bfs(y, x, visited_rgb, 1)
            rgb += 1

# 색약
for y in range(N):
    for x in range(N):
        if not visited_rb[y][x]:
            bfs(y, x, visited_rb, 0)
            rb += 1

print(rgb, rb)