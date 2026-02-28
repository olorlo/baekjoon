import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

from collections import deque

# 백준 1012번 유기농 배추

T = int(input())

# 상하좌우
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
            if g[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = 1
                dq.append([ny, nx])
            

for tc in range(T):
    M, N, K = map(int, input().split())
    # cabbage = [list(map(int, input().split())) for _ in range(K)]
    visited = [[0] * M for _ in range(N)]
    # print(cabbage[0])
    
    # g: 배추 심은 땅 리스트로 표현
    g = [[0] * M for _ in range(N)]
    for _ in range(K):
        X ,Y = map(int, input().split())
        g[Y][X] += 1

    cnt = 0

    for y in range(N):
        for x in range(M):
            if visited[y][x] == 0 and g[y][x] == 1:
                bfs(y, x)
                cnt += 1
                
    print(cnt)