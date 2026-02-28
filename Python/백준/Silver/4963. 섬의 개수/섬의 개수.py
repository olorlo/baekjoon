import sys
#sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
from collections import deque

# 백준 4963번 섬의 개수

dy = [-1, -1, -1, 1, 1, 1, 0, 0]
dx = [-1, 0, 1, -1, 0, 1, -1, 1]

def bfs(y, x):
    dq = deque([(y, x)])
    visited[y][x] = 1

    while dq:
        now_y, now_x = dq.popleft()
        for k in range(8):
            ny = now_y + dy[k]
            nx = now_x + dx[k]
            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue
            if not visited[ny][nx] and arr[ny][nx] == 1:
                visited[ny][nx] = 1
                dq.append([ny, nx])

# 테스트 케이스:
while True:
    w, h = map(int, input().split())
    # 테스트케이스 종료 조건
    if w == 0 and h == 0:
        break

    # 1: 땅, 0: 바다
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)
        




