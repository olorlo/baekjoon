# SWEA A형 기출 1949. 등산로 조성
T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# idx: 가장 높은 봉우리의 위치, cnt: K를 썼는지 안썻는지
def solve(cnt, path):
    global max_len
        
    now_y, now_x = path[-1]
    check = False
    for k in range(4):
        ny = now_y + dy[k]
        nx = now_x + dx[k]

        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue

        if visited[ny][nx]:
            continue

        # 주변에 나보다 작은 수가 존재 -> path에 추가
        if arr[ny][nx] < arr[now_y][now_x]:
            check = True
            visited[ny][nx] = True
            path.append((ny, nx))

            solve(cnt, path)

            # if cnt == 1:
            #     for a in range(1, K+1):
            #         if arr[ny][nx] - a < arr[now_y][now_x]:
            #             arr[ny][nx] -= a
            #             solve(cnt -1, path)
            #             arr[ny][nx] += a

            path.pop()
            visited[ny][nx] = False

        
        # 나보다 작은 수 없음 -> cnt 개수 체크 후 이동
        else:
            if cnt == 1:
                for a in range(1, K+1):
                    if arr[ny][nx] - a < arr[now_y][now_x]:
                        check = True
                        arr[ny][nx] -= a
                        path.append((ny, nx))
                        visited[ny][nx] = True
                        solve(cnt -1, path)
                        path.pop()
                        arr[ny][nx] += a
                        visited[ny][nx] = False
    # 주변을 바꿀 수 없음 -> 종료조건 
    if check == False:
        max_len = max(max_len, len(path))
        return 


for tc in range(1, T+1):
    # 지도 크기 N*N, 최대 공사 가능 깊이 K
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    
    # 일단 제일 높은 지형 찾기
    max_val = 0 
    high_idx = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] > max_val:
                max_val = arr[i][j]

    max_len = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_val:
                visited[i][j] = True
                solve(1, [(i, j)])
                visited[i][j] = False

    print(f'#{tc}', max_len)