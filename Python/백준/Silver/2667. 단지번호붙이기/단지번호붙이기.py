import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

from collections import deque

# 백준 2667번 단지 번호 붙이기
N = int(input())
arr = [list(input().strip()) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    global house
    dq = deque([(y, x)])
    visited[y][x] = 1
    house = 1

    while dq:
        now_y, now_x = dq.popleft()

        for k in range(4):
            ny = now_y + dy[k]
            nx = now_x + dx[k]

            if ny <0 or ny >= N or nx < 0 or nx >= N:
                continue
            if not visited[ny][nx] and int(arr[ny][nx]):
                visited[ny][nx] = cnt
                house += 1
                dq.append([ny, nx])

cnt = 0
house = 0
result = []

for y in range(N):
    for x in range(N):
        house = 0
        if not visited[y][x] and int(arr[y][x]) :
            cnt += 1
            bfs(y, x)
            result.append(house)

print(cnt)
result.sort()

for i in range(cnt):
    print(result[i])