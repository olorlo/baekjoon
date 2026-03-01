import sys
# sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

from collections import deque

# 백준 7569번 토마토
M, N, H = map(int, input().split())

dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 토마토 박스 입력
tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

def bfs(H, N, M):
    dq = deque()
    # 익은 토마토 모두 bfs에 넣음
    for z in range(H):
        for y in range(N):
            for x in range(M):
                # 익은 토마토일 때 전부 덱에 넣음
                if tomatoes[z][y][x] == 1:
                    dq.append((z, y, x))

    # 넣은 것들 중에서 아래위상하좌우 체크
    while dq:
        now_z, now_y, now_x = dq.popleft()

        for k in range(6):
            nz = now_z + dz[k]
            ny = now_y + dy[k]
            nx = now_x + dx[k]

            if nz < 0 or nz >= H or\
                ny < 0 or ny >= N or\
                nx < 0 or nx >= M:
                continue
            
            # 토마토 박스가 비었음 -> pass
            if tomatoes[nz][ny][nx] == -1:
                continue
            
            # 현재 익은 토마토인데 

            # 아래위상하좌우 중 안익은 토마토 존재 
            # -> 아래위상하좌우 토마토도 익음
            if tomatoes[nz][ny][nx] == 0:
                tomatoes[nz][ny][nx] = tomatoes[now_z][now_y][now_x] + 1
            
            # 현재 익은 토마토면 아래위상하좌우 모두 덱에 넣음
                dq.append([nz, ny, nx])

bfs(H, N, M)

max_day = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            # 하나라도 안익은 토마토 존재 -> -1 출력
            if tomatoes[z][y][x] == 0:
                print(-1)

                # 즉시 프로그램 종료
                exit(0)
            max_day = max(max_day, tomatoes[z][y][x])

print(max_day - 1)