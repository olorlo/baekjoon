import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

from collections import deque

# 백준 7562번 나이트의 이동
T = int(input())

dy = [-2, -2, 2, 2, -1, -1, 1, 1]
dx = [-1, 1, -1, 1, -2, 2, -2, 2]

def bfs(y, x):
    dq = deque([(y, x)])

    while dq:
        now_y, now_x = dq.popleft()
        if now_y == go_y and now_x == go_x:
            break
        for k in range(8):
            ny = now_y + dy[k]
            nx = now_x + dx[k]
            if ny < 0 or ny >= l or nx < 0 or nx >= l:
                continue
            if not visited[ny][nx]:
                dq.append([ny, nx])
                visited[ny][nx] = visited[now_y][now_x] + 1


for _ in range(T):
    l = int(input())
    y, x = map(int, input().split())
    go_y, go_x = map(int, input().split())

    visited = [[0]*l for _ in range(l)]
    bfs(y, x)
    print(visited[go_y][go_x])