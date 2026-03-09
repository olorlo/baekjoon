import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

# 백준 14502번 연구소

# 상하좌우 이동
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 바이러스 확산 bfs
def bfs():
    dq = deque()

    # 코테에서 많이 쓰는 깊은 복사 방법
    # 벽을 세운 상태 복사
    virus = [row[:] for row in arr]

    # 현재 바이러스 위치를 덱에 넣음
    for i in range(N):
        for j in range(M):
            if virus[i][j] == 2:
                dq.append((i, j))

    # 현재 바이러스 위치를 기준으로 바이러스 확산
    while dq:
        now_y, now_x = dq.popleft()
        
        # 상하좌우 체크해서 주변에 0이 있으면 바이러스 확산시킴
        for k in range(4):
            ny = now_y + dy[k]
            nx = now_x + dx[k]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            
            if virus[ny][nx] == 0:
                virus[ny][nx] = 2
                dq.append((ny, nx))

    # 안전 영역 개수 세기 
    cnt = 0
    for i in range(N):
        for j in range(M):
            if virus[i][j] == 0:
                cnt += 1
    return cnt

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 벽 만들기 
def make_wall(cnt, start):
    global safe

    # 벽 3개가 세워지면 바이러스 확산 실행
    if cnt == 3:
        # 안전 영역 최대값 계산
        safe = max(bfs(), safe)
        return
    
    # 벽 무한 생성 ㅋㅋ
    for idx in range(start, N*M):
        y = idx // M
        x = idx % M
        # 모든 칸 탐색해서 0이면 벽 만들기
        if arr[y][x] == 0:
            arr[y][x] = 1

            # 다음 벽 세우기
            make_wall(cnt + 1, idx+1)

            # 백트래킹 (벽 다시 제거 후 다시 생성하기 위한 도약)
            arr[y][x] = 0

# 벽을 먼저 세우고 bfs로 최단 거리 탐색
safe = 0
make_wall(0, 0)

# 결과
print(safe)