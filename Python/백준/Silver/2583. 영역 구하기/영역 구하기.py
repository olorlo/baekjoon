import sys
# sys.stdin = open("input.txt", 'r')

# 백준 dfs일 경우 무조건 추가해준다.
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 백준 2583번 영역구하기
M, N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(K)]
result = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)] 

cnt = 0
area = 0

# 상하우좌
dy = [1,-1,0,0]
dx = [0,0,1,-1]

def dfs(y, x):
    global area
    # 방문 표시
    visited[y][x] = 1

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]    
        if ny < 0 or ny >= M or nx < 0 or nx >=N:
            continue
        if result[ny][nx] == 0 and not visited[ny][nx]:
            area += 1
            dfs(ny, nx)
            
    # 종료 조건: 다 돌았는데, 더 이상 갈데가 없다. 
    return 

# 0인 부분 발견
# dfs 시작
# 연결된 0의 개수 cnt
# 영역 개수 + 1
# 넓이 저장

# 좌표로만 주어진 상황이니까 배열 만들기
for x1, y1, x2, y2 in arr:
    for y in range(y1, y2):
        for x in range(x1, x2):
            result[y][x] = 1

result_area = []

# result 중 0인 곳 찾고, 
# 방문되지 않았다면 방문해서 상하좌우 체크
# 그 다음 갈 수 있는 곳으로 계속 이동 후 갈 곳 없으면 dfs 종료 
# 종료 한 뒤 area 저장
# 구역 수 + 1
for i in range(M):
    for j in range(N):
        if result[i][j] == 0 and not visited[i][j]:
            area = 1
            dfs(i,j)
            result_area.append(area)
            cnt += 1

# print(*result)   
print(cnt)
print(*sorted(result_area))