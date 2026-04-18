# SWEA A형 기출 1767. 프로세서 연결하기 

T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(idx, core_cnt, length):
    global min_len, max_core

    # 가지치기
    # 앞으로 남은 코어를 전부 다 연결해도 지금까지 만든 max_core보다 작으면 
    # 계산할 필요도 없다.
    if core_cnt + (len(cores)-idx) < max_core:
        return 

    # 종료 조건
    if idx == len(cores):
        if core_cnt > max_core:
            max_core = core_cnt
            min_len = length
        elif core_cnt == max_core:
            min_len = min(min_len, length)
        return
    
    # 현재 코어 
    now_y, now_x = cores[idx]

    for k in range(4):
        ny, nx = now_y, now_x
        # 진행 방향 
        path = []

        # 진행 방향 체크
        while True:
            ny += dy[k]
            nx += dx[k]

            # 경계 처리
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                break

            # 진행방향에 core(1), 전선(2) 존재 -> 버려
            if arr[ny][nx] != 0:
                path = []
                break

            path.append((ny, nx))

        # 연결 o
        if path:

            # 전선 설치
            for py, px in path:
                arr[py][px] = 2

            dfs(idx+1, core_cnt+1, length+len(path))
            
            # 복구
            for py, px in path:
                arr[py][px] = 0
        
    # 연결 x
    dfs(idx+1, core_cnt, length)

for tc in range(1, T+1):
    N = int(input())

    # 0: 빈 셀, 1: core
    arr = [list(map(int, input().split())) for _ in range(N)]

    # core 리스트 만들기
    cores = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            
            if arr[i][j] == 1:
                cores.append((i, j))

    min_len = float('inf')
    max_core = 0
    dfs(0, 0, 0)
            
    print(f'#{tc}', min_len)