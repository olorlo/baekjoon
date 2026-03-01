import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

from collections import deque

# 백준 7576번 토마토
M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(N, M):
    dq = deque()

    for y in range(N):
        for x in range(M):
            # 익은 토마토라면 덱에 넣음
            if tomatoes[y][x] == 1:
                dq.append((y, x))

    # 익은 토마토에 대해서 상하좌우 체크
    while dq:
        now_y, now_x = dq.popleft()

        for k in range(4):
            ny = now_y + dy[k]
            nx = now_x + dx[k]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            if tomatoes[ny][nx] == 0:
                tomatoes[ny][nx] = tomatoes[now_y][now_x] + 1

                dq.append((ny, nx))
    
bfs(N, M)

max_day = 0

for y in range(N):
    for x in range(M):
        # 하나라도 익지 않은 토마토 존재
        if tomatoes[y][x] == 0:
            print(-1)
            exit(0)

        max_day = max(max_day, tomatoes[y][x])

print(max_day - 1)