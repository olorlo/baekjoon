import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

# 백준 3055번 탈출

R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 고슴도치가 이동하는 코드
# 만약 물이랑 도치가 만나면 그 값 버려야됨
def move():
    water = deque()
    dochi = deque()

    for i in range(R):
        for j in range(C):
            # 물 초기위치 저장
            if arr[i][j] == '*':
                water.append((i, j))

            # 도치 초기위치 저장
            if arr[i][j] == 'S':
                dochi.append((i, j))

    while dochi:
        
        # 물 먼저 확산
        for _ in range(len(water)):
            water_y, water_x = water.popleft()

            for k in range(4):
                ny = water_y + dy[k]
                nx = water_x + dx[k]
                if ny < 0 or ny >= R or nx < 0 or nx >= C:
                    continue
                if arr[ny][nx] == '.':
                    arr[ny][nx] = '*'
                    water.append((ny, nx))

        # 고슴도치 이동
        for _ in range(len(dochi)):
            dochi_y, dochi_x = dochi.popleft()
            for k in range(4):
                ny = dochi_y + dy[k]
                nx = dochi_x + dx[k]

                if ny < 0 or ny >= R or nx < 0 or nx >= C:
                    continue

                # 도치가 굴로 들어감
                if arr[ny][nx] == 'D':
                    return visited[dochi_y][dochi_x] + 1
                
                if arr[ny][nx] == '.' and not visited[ny][nx]:
                    visited[ny][nx] = visited[dochi_y][dochi_x] + 1
                    dochi.append((ny, nx))

    # 도치가 굴을 못찾음
    return 'KAKTUS'


result = move()
print(result)