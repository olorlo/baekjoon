import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

from collections import deque

# 백준 2589 보물섬
N, M = map(int, input().split())
treasure = [list(input().strip()) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

max_distance = 0 

def bfs(y, x):
    dq = deque([(y, x)])
    visited[y][x] = 1
    max_dist = 0

    while dq:
        now_y, now_x = dq.popleft()

        for k in range(4):
            ny = now_y + dy[k]
            nx = now_x + dx[k]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            if not visited[ny][nx] and treasure[ny][nx] == 'L':
                # 최단 거리 계산
                visited[ny][nx] = visited[now_y][now_x] + 1
                # 최단 거리이면서 육지 중 제일 긴 거리 계산 
                max_dist = max(max_dist, visited[ny][nx])
                dq.append([ny, nx])

    return max_dist

for y in range(N):
    for x in range(M):
        distance = 0
        if treasure[y][x] == 'L':
            # 모든 y, x에 대해서 L인지 체크
            visited = [[0]* M for _ in range(N)]

            # 가장 긴 시간이 걸리는 육지 계산
            max_distance = max(bfs(y, x), max_distance)

# 처음에 visited = 1이기때문에 1 빼줌
print(max_distance - 1)